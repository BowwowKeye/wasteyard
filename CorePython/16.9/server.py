# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 13:54:21 2018

@author: 37580
"""
from socket import *
from multiprocessing import Process, Manager
import sys
import os


def ReadytoSend(fileno):   #pass stdin to subprocess
    sys.stdin=os.fdopen(fileno)
    while True:
        reply=input()
        if not reply or reply=='exit':
            break
        reply='server > %s' % reply
        for item in wasteyard.keys():
            wasteyard[item][0].send(bytes(reply,'utf-8'))
    reply='server exit'
    for item in wasteyard.keys():
        wasteyard[item][0].send(bytes(reply,'utf-8'))
        wasteyard[item][0].close()
        wasteyard[item][1]=0
        
        
    
def WaitforReceive(client,addr):
    while True:
        data=client.recv(BUFSIZ)
        
        if not data or data.decode(encoding='utf-8')=='exit':
            data='%s exited' % addr
            print(data)
            for item in wasteyard.keys():
                if item!=str(addr):
                    wasteyard[item][0].send(bytes(data,'utf-8'))
            client.close()
            wasteyard[str(addr)][1]=0
            break
        
        data='%s > %s' % (str(addr),data.decode(encoding='utf-8'))
        print(data)
        for item in wasteyard.keys():
            if item != addr and wasteyard[str(addr)][1]==1:
                wasteyard[item][0].send(bytes(data,'utf-8'))
                


    
if __name__=='__main__':
    HOST=''
    PORT=2000
    BUFSIZ=1024
    ADDR=(HOST,PORT)
    fn=sys.stdin.fileno()
    wasteyard=Manager().dict()
    CTserver=socket(AF_INET,SOCK_STREAM)
    CTserver.bind(ADDR)
    CTserver.listen(5)
    flag=0
    print('server start')
    while True:
        CTclient,addr=CTserver.accept()
        print('connection established with',addr)
        RecPro=Process(target=WaitforReceive,args=(CTclient,addr))
        wasteyard[str(addr)]=[CTclient,1]
        RecPro.start()
        
        if flag==0:
            SenPro=Process(target=ReadytoSend,args=(fn,))
            SenPro.start()
            flag=1
            
        for item in wasteyard.keys():   #I'm not sure, the dict changed during iterator
            if wasteyard[item][1]==0:
                del wasteyard[item] 
        if not wasteyard:
            flag=0
            SenPro.join()
        
       
    CTserver.close()


    
