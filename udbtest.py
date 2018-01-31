import socket
import _thread
import tkinter

UDP_IP = "192.168.4.1"
UDP_PORT = 9000
MSG = ""

global sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def udplistener():
    while 1:
        print("attesa")
        data, socketsrc = sock.recvfrom(1024)
        print(data.decode())

def udpsender():
    while 1:
        data = input('comando')
        print("invio %s" % data)
        sock.sendto(bytes('%s\n' % data, 'utf-8'), (UDP_IP, UDP_PORT))

try:
    _thread.start_new_thread(udplistener, ())
    _thread.start_new_thread(udpsender, ())
except:
    print("Error: unable to start thread")

while 1:
    pass
