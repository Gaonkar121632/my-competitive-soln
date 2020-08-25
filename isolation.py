testCase=int(input())
allInputs=[]
for ele in range(0,testCase):
    temp=[]
    arr1 = list(map(int, input().split()))
    strr=input()
    for x in range(0,arr1[1]):
        temp.append(int(input()))
    allInputs.append([arr1[1],strr,temp])

for sample in allInputs:
    hashDic={}
    uniqueEle=set(sample[1])
    for x in uniqueEle:
        hashDic[x]=sample[1].count(x)    
    for val  in sample[2]:
        totalCount=0
        for key in hashDic:
            if hashDic[key]-val>0:
                totalCount+=hashDic[key]-val
            
        print(totalCount)