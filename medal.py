rawInputs=[]
testInput=int(input())
for x in range(0,testInput):
    dummy=input()
    arr=list(map(int, input().split()))
    rawInputs.append(arr)



for allInputs in rawInputs:
    while len(allInputs)>2:
        computArr=allInputs[0:3]
        computArr.sort()
        allInputs.remove(computArr[1])

    print(*allInputs,sep=' ')
