# allInputs=[[4,['a','b','b','c','a']]]
testCase=int(input())
allInputs=[]
for ele in range(0,testCase):
    tempArr=[]
    arr1 = list(map(int, input().split()))
    arr2 = list(input())
    tempArr.append(arr1[1])
    tempArr.append(arr2)
    allInputs.append(tempArr)

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for element in allInputs:
    target=element[0]
    # numArr=list(map(lookup,element[1]))
    count=0
    length=len(element[1])
    for i in range(0,length):
        summ=0
        while i>-1 and summ<target:
            summ=summ+alphabet.index(element[1][i])+1
            i=i-1
            if  summ==target:
                count=count+1
    print(count)