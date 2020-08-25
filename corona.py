testCase = input()
allInputs = []
for x in range(0,int(testCase)):
    dummpy=input()
    arr1 = list(map(int, input().split()))
    allInputs.append(arr1)

for sample in allInputs:
    count=0
    flag=False
    result="YES"
    for x in sample:
        if x==1 and not flag:
            flag=True
        elif x==0 and flag:
            count+=1
        elif x==1 and count<6:
            result="NO"
            break
        if count>=6:
            count=0
            flag=False
    print(result)
    