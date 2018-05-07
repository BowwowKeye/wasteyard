import os
import sys
import re
db=[]
def filescan(filename):
    f=open(filename,'r')
    for line in f:
        if re.match(r'r*[\'"]',line.strip()):
            db.append(os.getcwd()+'/'+filename)
            break
        else:
            s=line.strip()
            if s=='' or s[0]!='#':
                break
    f.close()

def dirscan(dirname):
    if os.path.isdir(dirname):
        for files in os.listdir(dirname):
            dirscan(dirname+'/'+files)
    else:
        filescan(dirname)
if __name__=='__main__':
    for dirpath in sys.path:
        try:
            os.chdir(dirpath)
            for files in os.listdir(os.getcwd()):
                dirscan(files)
        except(OSError):
            continue
    for item in db:
        print item    
