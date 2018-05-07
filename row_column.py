import sort
length=123
column=13
ran=sort.randomlist(1,10000,length)
print ran
for i in range(0,length/column):
    for j in range(0,column):
        print '%8d' % ran[i+j*length/column],
    print
