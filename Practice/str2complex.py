string=raw_input('please enter your number:\n')
part=[]
for i in range(0,len(string)):
    if (string[i] in '+-') and (string[i-1:i]!='E'):
        part.append(i)
if len(part)!=0 and part[0]>0 or len(part)>1:
    imag=string[part[-1]:-1]
    real=string[0:part[-1]] 
elif string[-1] in 'ij':
    imag=string[0:-1]
    real=0
else:
    real=string
    imag=0

print complex(float(real),float(imag))
