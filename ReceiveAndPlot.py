#!/usr/bin/env python
"""
ReceiveAndPlot example for LSL
This example shows data from all found outlets in realtime.
It illustrates the following use cases:
- efficiently pulling data, re-using buffers
- automatically discarding older samples
- online postprocessing
"""

import numpy as np
import math
import pylsl
import pyqtgraph as pg
from typing import List
import xml.etree.ElementTree as ET

# Basic parameters for the plotting window
plot_duration = 5  # how many seconds of data to show
update_interval = 60  # ms between screen updates
pull_interval = 500  # ms between each pull operation


class Inlet:
    """Base class to represent a plottable inlet"""

    def __init__(self, info: pylsl.StreamInfo):
        # create an inlet and connect it to the outlet we found earlier.
        # max_buflen is set so data older the plot_duration is discarded
        # automatically and we only pull data new enough to show it

        # Also, perform online clock synchronization so all streams are in the
        # same time domain as the local lsl_clock()
        # (see https://labstreaminglayer.readthedocs.io/projects/liblsl/ref/enums.html#_CPPv414proc_clocksync)
        # and dejitter timestamps
        self.inlet = pylsl.StreamInlet(info, max_buflen=plot_duration,
                                       processing_flags=pylsl.proc_clocksync | pylsl.proc_dejitter)
        # store the name and channel count
        self.name = info.name()
        self.channel_count = info.channel_count()

    def pull_and_plot(self, plot_time: float, plt: pg.PlotItem):
        """Pull data from the inlet and add it to the plot.
        :param plot_time: lowest timestamp that's still visible in the plot
        :param plt: the plot the data should be shown on
        """
        # We don't know what to do with a generic inlet, so we skip it.
        pass


class DataInlet(Inlet):
    """A DataInlet represents an inlet with continuous, multi-channel data that
    should be plotted as multiple lines."""
    dtypes = [[], np.float32, np.float64, None, np.int32, np.int16, np.int8, np.int64]

    def __init__(self, info: pylsl.StreamInfo, plt: pg.PlotItem):
        super().__init__(info)
        # calculate the size for our buffer, i.e. two times the displayed data
        bufsize = (2 * math.ceil(info.nominal_srate() * plot_duration), info.channel_count())
        self.buffer = np.empty(bufsize, dtype=self.dtypes[info.channel_format()])
        empty = np.array([])
        # create one curve object for each channel/line that will handle displaying the data
        self.curves = [pg.PlotCurveItem(x=empty, y=empty, autoDownsample=True) for _ in range(self.channel_count)]
        for curve in self.curves:
            plt.addItem(curve)

    def pull_and_plot(self, plot_time, plt):
        # pull the data
        _, ts = self.inlet.pull_chunk(timeout=0.0,
                                      max_samples=self.buffer.shape[0],
                                      dest_obj=self.buffer)
        # ts will be empty if no samples were pulled, a list of timestamps otherwise
        if ts:
            ts = np.asarray(ts)
            y = self.buffer[0:ts.size, :]
            this_x = None
            old_offset = 0
            new_offset = 0
            for ch_ix in range(self.channel_count):
                # we don't pull an entire screen's worth of data, so we have to
                # trim the old data and append the new data to it
                old_x, old_y = self.curves[ch_ix].getData()
                # the timestamps are identical for all channels, so we need to do
                # this calculation only once
                if ch_ix == 0:
                    # find the index of the first sample that's still visible,
                    # i.e. newer than the left border of the plot
                    old_offset = old_x.searchsorted(plot_time)
                    # same for the new data, in case we pulled more data than
                    # can be shown at once
                    new_offset = ts.searchsorted(plot_time)
                    # append new timestamps to the trimmed old timestamps
                    this_x = np.hstack((old_x[old_offset:], ts[new_offset:]))
                # append new data to the trimmed old data
                this_y = np.hstack((old_y[old_offset:], y[new_offset:, ch_ix] - ch_ix))
                # replace the old data
                self.curves[ch_ix].setData(this_x, this_y)


class MarkerInlet(Inlet):
    """A MarkerInlet shows events that happen sporadically as vertical lines"""

    def __init__(self, info: pylsl.StreamInfo):
        super().__init__(info)

    def pull_and_plot(self, plot_time, plt):
        # TODO: purge old markers
        strings, timestamps = self.inlet.pull_chunk(0)
        if timestamps:
            for string, ts in zip(strings, timestamps):
                plt.addItem(pg.InfiniteLine(ts, angle=90, movable=False, label=string[0]))


class EEGReceive_Plot(object):
    """docstring for EEGReceive_Plot"""

    def __init__(self, arg):
        super(EEGReceive_Plot, self).__init__()
        print(plot_duration)
        self.arg = arg
        self.counter = 0
        self.inlets: List[Inlet] = []
        self.stt = False
        self.saving = True
        print("looking for streams")
        streams = pylsl.resolve_streams()
        # Create the pyqtgraph window
        self.pw = pg.PlotWidget(title='EEG Plot')
        self.pw.setYRange(-2000, 2000, padding=0)
        self.plt = self.pw.getPlotItem()
        self.plt.enableAutoRange(x=False, y=False)

        # iterate over found streams, creating specialized inlet objects that will
        # handle plotting the data
        for stream in streams:
            if stream.name() == "EmotivDataStream-EEG":
                self.stt = True
                self.inlet = DataInlet(stream, self.plt)
        if len(self.inlets) > 0:
            self.stt = True

    def scroll(self):
        """Move the view so the data appears to scroll"""
        # We show data only up to a timepoint shortly before the current time
        # so new data doesn't suddenly appear in the middle of the plot
        fudge_factor = pull_interval * .002
        plot_time = pylsl.local_clock()
        self.pw.setXRange(plot_time - plot_duration + fudge_factor, plot_time - fudge_factor)

    def update(self):
        # print("EEG update")
        # Read data from the inlet. Use a timeout of 0.0 so we don't block GUI interaction.
        if not self.stt:
            return
        try:
            mintime = pylsl.local_clock() - plot_duration
            # call pull_and_plot for each inlet.
            # Special handling of inlet types (markers, continuous data) is done in
            # the different inlet classes.
            self.inlet.pull_and_plot(mintime, self.plt)
        except Exception as e:
            self.stt = False
            print(e, "error in inlet EEG")

    def signalStt(self):
        return self.stt

    def updateSaving(self):
        self.saving = True


class ETReceive(object):
    """docstring for ETReceive"""

    def __init__(self, arg):
        super(ETReceive, self).__init__()
        self.arg = arg
        self.stt = False
        streams = pylsl.resolve_stream()
        for stream in streams:
            if stream.name() == "Unity.ExampleStream":
                self.inlet = pylsl.StreamInlet(stream)
                self.stt = True

        self.listDataET = [['(0, 0, 0) : NONE : NONE']]
        self.lSample = []
        self.lTimeStamp = []
        self.saving = False

    def update(self):
        try:
            if self.stt:
                sample, timestamp = self.inlet.pull_sample()
            else:
                sample = ['(0, 0, 0) : NONE : NONE']
                timestamp = 0
            # print(sample, timestamp)
            # stop
            self.listDataET.append(sample)
            if self.saving:
                self.lSample.append(sample)
                self.lTimeStamp.append(timestamp)
        except Exception as e:
            print(e, "error in inlet ET")
            self.stt = False
        # print("update ET")

    def signalStt(self):
        return self.stt

    def updateSaving(self):
        self.saving = True

    def getSavingData(self):
        return [self.lSample, self.lTimeStamp]


class EEGReceive(object):
    """docstring for ETReceive"""

    def __init__(self, arg):
        super(EEGReceive, self).__init__()
        self.arg = arg
        streams = pylsl.resolve_stream()
        for stream in streams:
            if stream.name() == "EmotivDataStream-EEG":
                self.inlet = pylsl.StreamInlet(stream)

        self.listSaving = []
        self.lData = []
        self.lTimeStamp = []
        self.rcdTime = 0
        self.root = ET.fromstring(self.inlet.info().as_xml())
        self.errorUpdate = 0

    def update(self):
        try:
            # lastTime = 0
            # if len(self.lTimeStamp) > 0:
            #     lastTime = self.lTimeStamp[-1]
            samples, timestamps = self.inlet.pull_chunk()
            if len(timestamps) > 0:
                for idx, _ in enumerate(timestamps):
                    self.lData.append(samples[idx])
                    self.lTimeStamp.append(timestamps[idx])
            if len(self.lTimeStamp) > 0:
                self.rcdTime = self.lTimeStamp[-1] - self.lTimeStamp[0]

        except Exception as e:
            # print(e, "Error in inlet EEG Rec: ", self.errorUpdate)
            self.errorUpdate += 1
        # print("update EEG")

    def getSavingData(self):
        return [self.lData, self.lTimeStamp]

    def getLastRcdSample(self):
        return [self.lData[-1], self.lTimeStamp[-1]]

    def getFirstRcdSample(self):
        return [self.lData[0], self.lTimeStamp[0]]

    def getInfo(self):
        info = self.root[17][1]
        lInfo = []
        for x in info:
            lInfo.append(x[0].text)
        return lInfo

    def getRate(self):
        rate = self.root.find("nominal_srate").text
        return int(float(rate))

# if __name__ == "__main__":
#     EEGReceive_Plot("none")
