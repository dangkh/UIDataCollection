import socket
import time
s = socket.create_connection(("localhost", 22345))

s.sendall(b"select all\n")
s.recv(10)
s.sendall(b"filename {root:C:\\Data\\} {template:test%b.xdf}\n")
s.recv(10)
s.sendall(b"start\n")
s.recv(10)
time.sleep(5)
s.sendall(b"stop\n")