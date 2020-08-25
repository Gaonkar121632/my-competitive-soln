inputArr=[2,3,4,5,8,7,1,0,6]

def Partition(Arr,start,end):
    i=start-1
    pivote=Arr[end]
    for j in range(start,end):
        if Arr[j]<pivote:
            i+=1
            Arr[i],Arr[j]=Arr[j],Arr[i]
    Arr[i+1],Arr[end]=Arr[end],Arr[i+1]
    return i+1


def Quick_sort(Arr,start,end):
    if start>=end:
        # print(Arr)
        return
    
    p=Partition(Arr,start,end)
    Quick_sort(Arr,start,p-1)
    Quick_sort(Arr,p+1,end)


Quick_sort(inputArr,0,len(inputArr)-1)

print(inputArr)