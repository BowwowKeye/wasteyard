import time
import hashlib
import pickle
import shelve

db=shelve.open('shelve')

def newuser():
    global db
    while True:
        username=raw_input('username:\n')
        if username in db:
            print 'username already exist'
        else:
            while True:
                password=raw_input('password:\n')
                if password=='':
                    print 'password can\'t be empty'
                else:
                    break
            break
    db[username]=[]
    db[username]+=[hashlib.sha1(password).hexdigest()] 
    db[username]+=[time.time()]
def olduser():
    global db
    username=raw_input('username:\n')
    password=raw_input('password:\n')
    if password!='' and db.get(username)[0]==hashlib.sha1(password).hexdigest():
        if db.get(username)[1]!=None and time.time()-db.get(username)[1]<14400:
                print 'you have login at '+ time.ctime(db.get(username)[1])
        else:
            print 'login success,welcome back '+username
            print 'last login time: '+time.ctime(db.get(username)[1])
        db[username][1]=time.time()
    else:
        print 'username does\'nt exist or wrong password'
     
def login():
    note='''Make a choice:
            q(Q)uit
            l(L)ogin in
            r(R)egistration\n'''
    while True:
        choice=raw_input(note)
        choice=choice.strip()[0].lower()
        if choice=='q':
            break
        elif choice=='l':
            olduser()
        elif choice=='r':
            newuser()
        else:
            print 'unknown choice'
        print db
#############################################################
#load and save as a string
#def load():
#    try:
#        f=open('user_pass','r')        
#        for line in f:
#            s=line.strip()
#            item=s.split(':')
#            db[item[0]]=item[1]
#            timedb[item[0]]=float(item[2])
#        f.close()
#    except:
#        pass
#
#def save():
#    f=open('user_pass','w')
#    for item in db.keys():
#        f.write(item+':'+db[item]+':'+str(timedb[item])+'\n')
#    f.close()
############################################################
#load and save as pickle
#def load():
#    global db
#    global timedb
#    try:
#        f=open('pickle','rb')
#        db=pickle.load(f)
#        timedb=pickle.load(f)
#        f.close()
#        print db
#        print timedb
#    except:
#        print 'file load fail'
#
#def save():
#    f=open('pickle','wb')
#    pickle.dump(db,f)
#    pickle.dump(timedb,f)
#    f.close()
###########################################################
#shelve
  
if __name__=='__main__':
    login()
    db.close()
