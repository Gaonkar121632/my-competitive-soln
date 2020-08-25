testCase=int(input())
allInputs=[]
for ele in range(0,testCase):
    dummy=input()
    arr1 = list(map(int, input().split()))
    allInputs.append(arr1)

def findSeq(arr,i,summ):
    if i>=(len(arr)-1) or (arr[i+1]-arr[i])>2:
        return summ,i+1
    else:
        summ+=1
        return findSeq(arr,i+1,summ)


for sample in allInputs:
    Max=float("-inf")
    Min=float("inf")
    indx=0
    while indx<len(sample):
        summ,indx=findSeq(sample,indx,0)
        # print(summ,indx)

        if summ>Max:
            Max=summ
        if summ<Min:
            Min=summ
    print(Min+1,Max+1)
    

    
