from socket import *
HOST='192.168.1.122'
PORT=12345
BUFSIZ=1024
ADDR=(HOST,PORT)

clisock=socket(AF_INET,SOCK_STREAM)
clisock.connect(ADDR)

while True:
    data=raw_input('>')
    if not data:
        break
    clisock.send(data)
    data=clisock.recv(BUFSIZ)
    if not data:
        break
    print data

clisock.close()

