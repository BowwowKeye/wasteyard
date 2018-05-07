#!/usr/bin/env python
from random import randint,choice
from string import ascii_lowercase
from sys import maxint
from time import ctime

doms=('com','edu','net','org','gov')
f=open('data.txt','w')
for i in range(randint(5,10)):
    dtint=randint(0,2147483647)
    dtstr=ctime(dtint)
    shorter=randint(4,7)
    em=''
    for j in range(shorter):
        em+=choice(ascii_lowercase)
    longer=randint(shorter,12)
    dn=''
    for j in range(longer):
        dn+=choice(ascii_lowercase)
    f.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr,em,dn,choice(doms),dtint,shorter,longer))
f.close()
