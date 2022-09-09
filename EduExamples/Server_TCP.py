import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8888))
s.listen(5) #ограничение на 5 подлюченных клиентов, и ожидающих ответа
while True:
    try:
        client, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    else:
        result = client.recv(1024)
        print('Message:', result.decode('utf-8'))
