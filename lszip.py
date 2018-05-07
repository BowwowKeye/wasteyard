import tarfile
import os
tar=tarfile.open('keys.tar','r')
os.mkdir('keys')
os.chdir('keys')
filelist=['revert.py','test.py','sort.py','user_pass']
for item in filelist:
    if 'py' in item.split('.'):
        tar.extractall(item)
tar.close()
