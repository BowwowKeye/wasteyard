def swap(x,y):
    t=x
    x=y
    y=t
def GCD(x,y):
    if x<y:
        swap(x,y)
    while y!=0:
        r=x%y
        x=y
        y=r
    return x
def LCM(x,y):
    return x*y/GCD(x,y)
number=raw_input('input two number:\n')
lis=number.split()
x=int(lis[0])
y=int(lis[1])
print 'GCD:%d' % GCD(x,y)
print 'LCM:%d' % LCM(x,y)
