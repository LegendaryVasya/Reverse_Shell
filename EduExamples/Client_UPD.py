import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UPD, SOCk_STREAM для TCP

s.sendto(b'hi', ('localhost', 8888))
