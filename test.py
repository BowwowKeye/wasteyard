from socket import *
from select import select
import sys

def prompt():
    sys.stdout.write('<You>')
    sys.stdout.flush()

HOST='192.168.1.106'
PORT=5000
BUFSIZ=1024
ADDR=(HOST,PORT)

DTclient=socket(AF_INET,SOCK_STREAM)
DTclient.connect(ADDR)
print 'connected to',ADDR
listenlist=[sys.stdin,DTclient]
while True:
    reads,writes,errors=select(listenlist,[],[])
    for fd in reads:
        if fd==DTclient:
            data=DTclient.recv(BUFSIZ)
            if not data:
                print 'Disconnnected from server'
                sys.exit()
            else:
                sys.stdout.write(data)
                prompt()
        elif fd==sys.stdin:
            msg=sys.stdin.readline()
            DTclient.send(msg)
            prompt()
