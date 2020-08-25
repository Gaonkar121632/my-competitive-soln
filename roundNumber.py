# for i in range(90900,100000):
#     x=str(i)
#     temp=0
#     for j in x:
#         temp=temp+int(j)
#     if temp%10==0:
#         print(i)


# n=['9999']

testCase = int(input())
inputArr=[]
for x in range(0, testCase):
    data=input()
    inputArr.append(data)


def findSum(numb):
    temp=0
    for j in numb:
        temp=temp+int(j)
    return temp

for i in inputArr:
    totalSum=findSum(i)
    sumToAppend=10-(int(totalSum)%10) if len(str(totalSum))>1 else 10-totalSum
    if sumToAppend==10:
        sumToAppend=0
    print(i+str(sumToAppend))