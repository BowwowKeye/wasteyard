#!/usr/bin/env python

import os

def Write():
    while True:
        filename=raw_input('Please enter a file name:\n')
        try:
            open(filename,'r')
            print "file already exists"
        except IOError, e:
            break

    output=[]
    print "input '.' to exit"
    while True:
        line=raw_input('>')
        if line=='.':
            break
        else:
            output.append(line)

    print output

    fhandle=open(filename,'w')
    fhandle.write('\n'.join(output))
    fhandle.close()
    print 'DONE'

def Read():
    print
    filename=raw_input('input the file name you wnat to display')
    
    if os.path.exists(filename):
        fhandle=open(filename,'r')
    else:
        print "file not exist"
        exit()
 
    for item in fhandle:
        print item.strip()
    fhandle.close()

while True:
    operation=raw_input("what do you want to do with the file? write(W),read(R)")
    if operation=="write" or operation=="W":
        Write()
        exit()
    elif operation=="read" or operation=="R":
        Read()
        exit()
    else:
        print "please input write(W) or read(R)"
    
