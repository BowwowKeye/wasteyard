import random
value=int(raw_input('The number to repeat[0-255]:\n'))
count=int(raw_input('Appear time:\n'))
size=int(raw_input('Bytes in the file:\n'))
f=open('create','w')
position=[]
if count>size:
    exit()
for i in range(count):
    point=random.randint(0,size-1)
    while point in position:
        point=random.randint(0,size-1)
    position.append(point)
print position
for i in range(size):
    if i in position:
        f.write(chr(value))
        continue
    randnumber=random.randint(0,255)
    while randnumber==value:
        randnumber=random.randint(0,255)
    f.write(chr(randnumber))
f.close()

