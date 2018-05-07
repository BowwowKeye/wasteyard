import os
import subprocess
import sys
import time
import re
def pipexec(commands,pipstdin=None):
    com=commands.split('|',1)
    if len(com)==1:
        print com[0],pipstdin,sys.stdout
        result=subprocess.Popen(re.split(r'[ ]*',com[0].strip()),stdin=pipstdin)
        return 0
    else:
        r,w=os.pipe()
        pid=os.fork()
        if pid:
            #in parent process
            os.close(w)
            r=os.fdopen(r)
            pipexec(com[1],r)
        else:
            #in child process
            os.close(r)
            w=os.fdopen(w,'w')
            print com[0],pipstdin,w
            subprocess.Popen(re.split(r'[ ]*',com[0].strip()),stdin=pipstdin,stdout=w)
            w.close() 
            sys.exit(0)
def main():
    while True:
        command=raw_input('keys$>>')
        pipexec(command)
        time.sleep(1)

main() 
