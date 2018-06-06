from threading import Thread
import random
import time

class ScanThread(Thread):
    def __init__(self,func,args):
        Thread.__init__(self)
        self.func=func
        self.args=args
        self.res=0

    def GetResult(self):
        return self.res

    def run(self):
        print('start at:',time.ctime(),';Thread:',self.name)
        self.res=self.func(*self.args)
        print('stop at:',time.ctime(),';Thread:',self.name)

def scanfile(text):
    count=0
    for letter in text:
        time.sleep(0.0001)
        if ord(letter)==num:
            count=count+1
    return count

    
def main():
    fd=open('char.dat','w')
    global num
    num=108
    length=19601
    times=238
    pos=[]
    while len(pos)<238:
        newpos=random.randint(0,length)
        if newpos not in pos:
            pos.append(newpos)
    for i in range(1,length+1):
        if i in pos:
            fd.write(chr(num))
        else:
            m=num
            while m==num:
                m=random.randint(0,255)
            fd.write(chr(m))
    fd.close()
    
    #start analysing file char.dat
    fd=open('char.dat','r')
    text=''.join(fd.readlines())
    length=len(text)
    threadnum=6
    threads=[]
    total=0
    for i in range(1,threadnum+1):
        start=(i-1)*length//threadnum
        if i==threadnum:
            stop=length
        else:
            stop=i*length//threadnum
        t=ScanThread(scanfile,(text[start:stop],))
        threads.append(t)

    for i in range(0,threadnum):
        threads[i].start()
    for i in range(0,threadnum):
        threads[i].join()
        total+=threads[i].GetResult()

    print('all Done at:',time.ctime())
    print('total=',total)
    
    

if __name__=='__main__':
    main()
