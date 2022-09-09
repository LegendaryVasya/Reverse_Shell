import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UPD, SOCk_STREAM для TCP

s.bind(('localhost', 8888))
result = s.recv(1024)
print('Message:', result.decode('utf-8'))
s.close()
