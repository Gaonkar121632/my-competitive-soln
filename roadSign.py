import math
testCase=int(input())
inputArr=[]
for inputValue in range(0,testCase):
    inputArr.append(int(input()))

for k in inputArr:
    powerOf=int("1"+('0'*k))
    # print(powerOf)
    count=0
    for i in range(0,powerOf):
        x=str(powerOf-i-1)
        inputArr=list(str(i))
        y=inputArr+list(x)
        mySet=set(y)
        if len(mySet)==2:
                # print(i,"===>",powerOf-i-1,"====>",len(mySet))
                count=count+1
    print(count)

