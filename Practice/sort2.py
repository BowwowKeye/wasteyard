import random
def randomlist(start,stop,length):
    randlist=[]
    for i in range(length):
	randlist.append(random.randint(start,stop))
    return randlist

def swap(a,index1,index2):
    if a[index1]!=a[index2]:
        a[index1]+=a[index2]
        a[index2]=a[index1]-a[index2]
        a[index1]=a[index1]-a[index2]

def partition(randlist,left,right,pivot):
    standard=randlist[pivot]
    Index=left
    swap(randlist,pivot,right)
    for i in range(left,right):
	if randlist[i]<=standard:
	    swap(randlist,i,Index)
            Index+=1
    swap(randlist,Index,right)
    return Index 

def quicksort(randlist,left,right):
    if left>=right:
        return 0
    Index=partition(randlist,left,right,(left+right)/2)
    quicksort(randlist,left,Index-1)
    quicksort(randlist,Index+1,right)
    return 0

def merge(randlist,assist,left,mid,right):
    move1=left
    move2=mid+1
    move=left
    while move1<=mid and move2<=right:
        if randlist[move1]<randlist[move2]:
	    assist[move]=randlist[move1]
	    move1+=1
        else:
            assist[move]=randlist[move2]
	    move2+=1
        move+=1
    while move1<=mid:
	assist[move]=randlist[move1]
	move1+=1
	move+=1
    while move2<=right:
	assist[move]=randlist[move2]
	move2+=1
	move+=1
    return 0



    

def mergesort(randlist,assist,left,right):
    if left>=right:
	return 0
    mergesort(randlist,assist,left,(left+right)/2)
    mergesort(randlist,assist,(left+right)/2+1,right)
    merge(randlist,assist,left,(left+right)/2,right)
    for i in range(left,right+1):
        randlist[i]=assist[i]
    return 0


if __name__=='__main__':
    result=randomlist(1,1000,20)    
    print result
    quicksort(result,0,len(result)-1)
    print result
    result2=randomlist(1,1000,20)
    print result2
    result3=result2
    assist=range(0,len(result2))
    mergesort(result2,assist,0,len(result2)-1)
    print result2
    quicksort(result3,0,len(result3)-1)
    print result3
