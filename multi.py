import os
import sys
import cv2
import queue
import threading
import time
from pylsl import StreamInfo, StreamOutlet


exitFlag = 0
parameters = { 'fps': 30.0,
               'width': 1920.0,
               'height': 1080.0,
               'brightness': 128.0,
               'contrast': 128.0,
               'saturation': 128.0,
               'hue': -1.0,
               'gain': 0.0,
               'exposure': -5.0 }

class myThread (threading.Thread):
   def __init__(self, threadID, name,):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting capture device " + self.name)
      capture(self.name, True)
      print ("Exiting capture device " + self.name)

def setDevParameters(cap, parameters):
   cap.set(cv2.CAP_PROP_FPS,           parameters['fps'])
   cap.set(cv2.CAP_PROP_FRAME_WIDTH,   parameters['width'])
   cap.set(cv2.CAP_PROP_FRAME_HEIGHT,  parameters['height'])
   cap.set(cv2.CAP_PROP_BRIGHTNESS,    parameters['brightness'])
   cap.set(cv2.CAP_PROP_CONTRAST,      parameters['contrast'])
   cap.set(cv2.CAP_PROP_SATURATION,    parameters['saturation'])
   cap.set(cv2.CAP_PROP_HUE,           parameters['hue'])
   cap.set(cv2.CAP_PROP_GAIN,          parameters['gain'])
   cap.set(cv2.CAP_PROP_EXPOSURE,      parameters['exposure'])

def listCapDev():
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
   n = k
   return n-1;

def capture(deviceID, record=False):
   global exitFlag
   global parameters
   print("deviceID: " + deviceID)
   frameCounter = 1
   cap_i = cv2.VideoCapture(int(deviceID))
   if not cap_i.isOpened():
      print("deviceID: " + deviceID + " is not opended.")
      return

   setDevParameters(cap_i, parameters)

   winName = 'Camera ' + str(deviceID)
   cv2.namedWindow(winName)

   if record:
      fps = cap_i.get(cv2.CAP_PROP_FPS)
      width = cap_i.get(cv2.CAP_PROP_FRAME_WIDTH)
      height = cap_i.get(cv2.CAP_PROP_FRAME_HEIGHT)
      filename = os.path.join("", 'Camera' + str(deviceID) + '.avi')
      fourcc = cv2.VideoWriter_fourcc(*'XVID')
      writer_i = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)))
      outlet = createOutlet(int(deviceID), filename)
   try:
      ret = True
      while exitFlag != 1 and ret:
         win_i = winName
         if cv2.getWindowProperty(win_i, cv2.WND_PROP_VISIBLE):
            ret, frame = cap_i.read()
            cv2.imshow(win_i, frame)
            if record:
               outlet.push_sample([frameCounter])
               writer_i.write(frame)
         else:
            ret = False
         frameCounter += 1
         cv2.waitKey(1)
   finally:
      cap_i.release()
      cv2.destroyAllWindows()
      state = ''

def createOutlet(index, filename):
   streamName = 'FrameMarker'+str(index+1)
   info = StreamInfo(name=streamName, type='videostream', channel_format='float32', channel_count=1, source_id=str(index))
   if sys.platform == "linux":
      videoFile = os.path.splitext(filename)[0]+'.ogv'
   else:
      videoFile = os.path.splitext(filename)[0]+'.avi'
   info.desc().append_child_value("videoFile", videoFile)
   return StreamOutlet(info)


numberDevices = listCapDev()
threads = []
threadID = 1

# Create new threads
for tName in range(numberDevices-1):
   thread = myThread(threadID, str(tName))
   thread.start()
   threads.append(thread)
   threadID += 1

if cv2.waitKey(1) & 0xFF == ord('q'):
   exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")