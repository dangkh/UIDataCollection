import os
import cv2
import threading
from pylsl import StreamInfo, StreamOutlet
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qimage2ndarray


class VideoRecorder:
    class myThread (threading.Thread):
        def __init__(self, threadID, name, func):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.func = func

        def run(self):
            print("Starting capture device " + self.name)
            self.func(self.name, True)
            print("Exiting capture device " + self.name)

    def __init__(self):
        self.exitFlag = 0
        self.parameters = {'fps': 30.0,
                           'width': 1920.0,
                           'height': 1080.0,
                           'brightness': 128.0,
                           'contrast': 128.0,
                           'saturation': 128.0,
                           'hue': -1.0,
                           'gain': 0.0,
                           'exposure': -5.0}
        self.numberDevices = 0
        self.threads = []
        self.threadID = 1
        self.savingDir = ""
        self.record = False
        self.createMeta = [False] * 10
        self.outlet = {}
        self.filename = {}
        self.writer = {}
        self.listCapDev()

    def cleanRecorder(self):
        self.exitFlag = 0
        self.numberDevices = 0
        self.threads = []
        self.threadID = 1
        self.listCapDev()

    def setDevParameters(self, cap):
        cap.set(cv2.CAP_PROP_FPS, self.parameters['fps'])
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.parameters['width'])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.parameters['height'])
        cap.set(cv2.CAP_PROP_BRIGHTNESS, self.parameters['brightness'])
        cap.set(cv2.CAP_PROP_CONTRAST, self.parameters['contrast'])
        cap.set(cv2.CAP_PROP_SATURATION, self.parameters['saturation'])
        cap.set(cv2.CAP_PROP_HUE, self.parameters['hue'])
        cap.set(cv2.CAP_PROP_GAIN, self.parameters['gain'])
        cap.set(cv2.CAP_PROP_EXPOSURE, self.parameters['exposure'])
        cap.set(cv2.CAP_PROP_CONVERT_RGB, 16)

    def listCapDev(self):
        k = 0
        while True:
            cap = cv2.VideoCapture(k, cv2.CAP_DSHOW)
            if not cap.isOpened():
                print("device " + str(k) + " is not opended.")
                break
            else:
                print("device " + str(k) + " is OPENDED.")
                cap.release()
            k += 1
            if k >= 2:
                break

        # print("total cam: ", k)
        self.numberDevices = k

    def capture(self, deviceID, record=False):

        iDID = int(deviceID)
        # print(" capture hihi deviceID: " + str(deviceID))
        frameCounter = 1
        cap_i = cv2.VideoCapture(int(deviceID), cv2.CAP_DSHOW)
        if not cap_i.isOpened():
            print("capture deviceID: " + str(deviceID) + " is not opended.")
            return
        # print('')

        self.setDevParameters(cap=cap_i)

        # winName = 'Camera ' + str(deviceID)
        # cv2.namedWindow(winName)
        fps = cap_i.get(cv2.CAP_PROP_FPS)
        print("FPS: ", fps)
        width = cap_i.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap_i.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        self.outlet[iDID] = self.createOutlet(iDID)

        try:
            ret = True
            # print("Exit", self.exitFlag)
            while self.exitFlag != 1 and ret:

                if self.record and not self.createMeta[iDID]:
                    self.filename[iDID] = os.path.join(self.savingDir, 'Camera' + str(deviceID) + '.avi')
                    self.writer[iDID] = cv2.VideoWriter(self.filename[iDID], fourcc, int(fps), (int(width), int(height)))
                    self.createMeta[iDID] = True
                    print("INIT")
                # win_i = winName
                if True:  # cv2.getWindowProperty(win_i, cv2.WND_PROP_VISIBLE):
                    ret, frame = cap_i.read()
                    self.outlet[iDID].push_sample([frameCounter])

                    if not self.record:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        image = qimage2ndarray.array2qimage(frame)
                        self.updateInThread(deviceID, image)
                    elif self.createMeta[iDID]:
                        # print(self.outlet)
                        self.writer[iDID].write(frame)
                else:
                    ret = False

                frameCounter += 1
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     self.exitFlag = 1
        finally:
            # self.writer[iDID].release()
            cap_i.release()
            cv2.destroyAllWindows()

    def createOutlet(self, index):
        streamName = 'Camera' + str(index)
        info = StreamInfo(name=streamName, type='videostream', channel_format='float32',
                          channel_count=1, source_id=str(index))
        # if sys.platform == "linux":
        #     videoFile = os.path.splitext(filename)[0] + '.ogv'
        # else:
        #     videoFile = os.path.splitext(filename)[0] + '.avi'
        # info.desc().append_child_value("videoFile", videoFile)
        return StreamOutlet(info)

    def beginRecord(self):
        self.cleanRecorder()
        for tName in range(self.numberDevices):
            thread = self.myThread(self.threadID, str(tName), self.capture)
            thread.start()
            self.threads.append(thread)
            self.threadID += 1

    def updateSavingDir(self, path):
        # self.record = True
        self.savingDir = path

    def stopRecord(self):
        self.exitFlag = 1
        # Wait for all threads to complete
        for t in self.threads:
            t.join()
        print("Exiting Main Thread")

    def setLabelImage(self, listLabel):
        self.listLabel = listLabel

    def updateInThread(self, deviceID, frame):
        # self.listLabel[int(deviceID)].setText(str(deviceID))
        # image = QtGui.QImage(bytes(frame), 50, 50, 3 * 50, QtGui.QImage.Format_RGB888)
        # pixmap = QtGui.QPixmap(image)
        w = self.listLabel[int(deviceID)].width()
        h = self.listLabel[int(deviceID)].height()
        # label->setPixmap(p.scaled(w,h,Qt::KeepAspectRatio));
        self.listLabel[int(deviceID)].setPixmap(QPixmap.fromImage(frame).scaled(w, h))


# record = VideoRecorder()
# record.beginRecord()
# time.sleep(5)
# record.stopRecord()
