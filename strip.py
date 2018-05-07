x=raw_input('enter your string\n')
x=list(x)
while x[0]==' ':
    del x[0]
while x[-1]==' ':
    del x[-1]
x=''.join(x)
print x+'hello'
