s=raw_input('please enter your number:\n')
dictionary=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
dictionary2=['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
output=''
low=int(s[-2:-1]+s[-1])
if 0<low<20:
    output= '%s%s' % (output,dictionary[low])
elif low>=20:
    if low%10!=0:
        output= '%s-%s' % (dictionary2[low/10-2],dictionary[low%10])
    else:
        output= '%s' % dictionary2[low/10-2]
if s[-3:-2]!='' and s[-3:-2]!='0':
    output= '%s hundred %s' % (int(s[-3]),output)
if s[-4:-3]!='' and s[-4:-3]!='0':
    output= '%s thousand  %s' % (int(s[-4]),output)

print output
