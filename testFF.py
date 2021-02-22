import subprocess
import time

pipe = subprocess.Popen("ffmpeg -y -f dshow -rtbufsize 1000M -s 1920x1080 -r 30 -i video=\"Logitech Webcam C930e\" -b:v 5M out.avi")
time.sleep(10)
pipe.terminate()
