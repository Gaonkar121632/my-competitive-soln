testCase=int(input())
inputValues=[]
for x in range(0,testCase):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    tempValue=0
    for x in arr2:
        tempValue=tempValue+x
    inputValues.append([arr1[1],tempValue])

# print(inputValues)

for value in inputValues:
    if value[0]<value[1]:
        print('No')
    else:
        print('Yes')
        

