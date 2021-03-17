import socket
HOST = "192.168.1.34"  # The server's hostname or IP address
PORT = 23233        # The port used by the server
while True:
    act = input("What action do you want? ")
    if(act == "1"):
        # Hieu chinh va luyen tap
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'OPEN_CALIBRATION')
    elif(act == "2"):
        # Mo ban phim ao
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'OPEN_KEYBOARD')
    elif(act == "3"):
        # Man hinh thu gian
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'OPEN_RELAXATION')