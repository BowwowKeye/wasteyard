import sys
f=open(sys.argv[1],'r')
for eachline in f:
    if eachline[0]=='#':
        continue
    else:
        print eachline
