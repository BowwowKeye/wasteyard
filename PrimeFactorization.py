def isPrima(num):
    for factor in range(2,num/2+1):
        if num%factor==0:
            return False
    else:
        return True

def factorize(num):
    return [factor for factor in range(2,num/2+1) if num%factor==0]

num=int(raw_input('Please enter a number:'))
if isPrima(num):
    print num
    exit()
PrimaFactor= [factor for factor in factorize(num) if isPrima(factor)]
result=[]
for factor in PrimaFactor:
    while num%factor==0:
        num/=factor
        result.append(factor)

print result
