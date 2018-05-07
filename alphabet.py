begin=int(raw_input('Enter begin value:'))
end=int(raw_input('Enter end value:'))
if begin>end or begin<0:
    print 'illegal range'
    exit()
if begin in range(32,127) or end in range(32,127):
    print ''
binwidth=len(bin(end))
for i in range(begin,end+1):
    print '%8d %12s %8o %8x' % (i,bin(i)[2:],i,i),
    if i in range(32,127):
        print '%8s' %chr(i)
    else:
        print

