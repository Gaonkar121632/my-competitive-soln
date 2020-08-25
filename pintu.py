rawInputs=[]
testInput=int(input())
for x in range(0,testInput):
    tmpArr=[]
    dummyA=list(map(int, input().split()))
    arrA=list(map(int, input().split()))
    arrB=list(map(int, input().split()))
    tmpArr.append(dummyA)
    tmpArr.append(arrA)
    tmpArr.append(arrB)
    rawInputs.append(tmpArr)

# print(rawInputs)

for sample in rawInputs:
    # print("--->",sample)
    hashMap={}
    data=sample[0]
    pintu=sample[1]
    fruits=sample[2]
    minimum=float("inf")
    for i in range(0,data[0]):
        if pintu[i] in hashMap:
            hashMap[pintu[i]]=hashMap[pintu[i]]+fruits[i]
        else : 
            hashMap[pintu[i]]=fruits[i]

    for ky in hashMap:
        minimum=hashMap[ky] if hashMap[ky]<minimum else minimum
    print(minimum)
        
