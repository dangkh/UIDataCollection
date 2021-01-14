import os
import sys
import cv2
import queue
import threading
import time
from pylsl import StreamInfo, StreamOutlet

class VideoRecorder:
   class myThread (threading.Thread):
      def __init__(self, threadID, name, func):
         threading.Thread.__init__(self)
         self.threadID = threadID
         self.name = name
         self.func = func
      def run(self):
         print ("Starting capture device " + self.name)
         self.func(self.name, True)
         print ("Exiting capture device " + self.name)

   def __init__(self):
      self.exitFlag = 0
      self.parameters = {  'fps': 30.0,
                           'width': 1920.0,
                           'height': 1080.0,
                           'brightness': 128.0,
                           'contrast': 128.0,
                           'saturation': 128.0,
                           'hue': -1.0,
                           'gain': 0.0,
                           'exposure': -5.0 }
      self.numberDevices = 0;
      self.threads = []
      self.threadID = 1
      self.listCapDev()

   def cleanRecorder(self):
      self.exitFlag = 0
      self.numberDevices = 0;
      self.threads = []
      self.threadID = 1
      self.listCapDev()

   def setDevParameters(self, cap):
      cap.set(cv2.CAP_PROP_FPS,           self.parameters['fps'])
      cap.set(cv2.CAP_PROP_FRAME_WIDTH,   self.parameters['width'])
      cap.set(cv2.CAP_PROP_FRAME_HEIGHT,  self.parameters['height'])
      cap.set(cv2.CAP_PROP_BRIGHTNESS,    self.parameters['brightness'])
      cap.set(cv2.CAP_PROP_CONTRAST,      self.parameters['contrast'])
      cap.set(cv2.CAP_PROP_SATURATION,    self.parameters['saturation'])
      cap.set(cv2.CAP_PROP_HUE,           self.parameters['hue'])
      cap.set(cv2.CAP_PROP_GAIN,          self.parameters['gain'])
      cap.set(cv2.CAP_PROP_EXPOSURE,      self.parameters['exposure'])

   def listCapDev(self):
      k = 0
      while True:
         cap = cv2.VideoCapture(k)
         if not cap.isOpened():
            print("device " + str(k) + " is not opended.")
            break
         else:
            print("device " + str(k) + " is OPENDED.")
            cap.release()
         k += 1
      self.numberDevices = k - 1

   def capture(self, deviceID, record=False):
      global exitFlag
      global parameters
      print("deviceID: " + str(deviceID))
      frameCounter = 1
      cap_i = cv2.VideoCapture(int(deviceID))
      if not cap_i.isOpened():
         print("deviceID: " + str(deviceID) + " is not opended.")
         return

      self.setDevParameters(cap=cap_i)

      winName = 'Camera ' + str(deviceID)
      #cv2.namedWindow(winName)

      if record:
         fps = cap_i.get(cv2.CAP_PROP_FPS)
         width = cap_i.get(cv2.CAP_PROP_FRAME_WIDTH)
         height = cap_i.get(cv2.CAP_PROP_FRAME_HEIGHT) 
         filename = os.path.join("", 'Camera' + str(deviceID) + '.avi')
         fourcc = cv2.VideoWriter_fourcc(*'XVID')
         writer_i = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)))
         outlet = self.createOutlet(int(deviceID), filename)
      try:
         ret = True
         while self.exitFlag != 1 and ret:
            #win_i = winName
            if True: # cv2.getWindowProperty(win_i, cv2.WND_PROP_VISIBLE):
               ret, frame = cap_i.read()
               #cv2.imshow(win_i, frame)
               if record:
                  outlet.push_sample([frameCounter])
                  writer_i.write(frame)
            else:
               ret = False

            frameCounter += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
               self.exitFlag = 1
      finally:
         cap_i.release()
         cv2.destroyAllWindows()

   def createOutlet(self, index, filename):
      streamName = 'FrameMarker'+str(index+1)
      info = StreamInfo(name=streamName, type='videostream', channel_format='float32', channel_count=1, source_id=str(index))
      if sys.platform == "linux":
         videoFile = os.path.splitext(filename)[0]+'.ogv'
      else:
         videoFile = os.path.splitext(filename)[0]+'.avi'
      info.desc().append_child_value("videoFile", videoFile)
      return StreamOutlet(info)

   def beginRecord(self):
      self.cleanRecorder()
      # Create new threads
      for tName in range(self.numberDevices-1):
         thread = self.myThread(self.threadID, str(tName), self.capture)
         thread.start()
         self.threads.append(thread)
         self.threadID += 1

   def stopRecord(self):
      self.exitFlag = 1
       # Wait for all threads to complete
      for t in self.threads:
         t.join()
      print ("Exiting Main Thread")



record = VideoRecorder()
record.beginRecord()