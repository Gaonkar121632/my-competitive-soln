allInputs=[]
test=int(input())
for x in range(0,test):
    dummy=input()
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    allInputs.append([arr1,arr2])

def filr(x,arr):
    for i in range(0,len(arr)):
        if arr[i]<x:
            return i
    return -1
    

for sample in allInputs:
    count=0
    for x in sample[0]:
        index=filr(x,sample[1])
        if index!=-1:
            count+=1
            index+=1
            sample[1]=sample[1][index:]
        else:
            break
    print(count)