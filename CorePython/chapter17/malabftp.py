from ftplib import FTP,error_perm
import os
def scandir(path):
    os.mkdir('files%s' % path)
    for item in f.nlst(path):
        if AbleTrans(item.split('/')[-1]):
            try:
                f.retrbinary('RETR %s' % item,open('files%s' % item,'wb').write)
            except error_perm as err:
                print(err)
                os.remove('files%s' % item)
                print('scan dir %s' % item)
                scandir(item)
                print('finished dir')
                       
def AbleTrans(name):
    part=name.split('.')
    if len(part)==1:
        return True
    elif part[len(part)-1] in Suffix:
        return True
    else:
        return False


os.mkdir('files')
Suffix=['pdf','txt']
f=FTP('qoqi.nju.edu.cn')
f.login('malabftp','d208d110')
scandir('/Books')
f.quit()
