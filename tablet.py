testCase = input()
mainArray=[]
costArray=[]
for x in range(0, int(testCase)):
    x,cost=input().split()
    costArray.append(int(cost))

    arry2=[]
    for target_list in range(0,int(x)):
        arr = list(map(int, input().split()))
        arry2.append(arr)
    mainArray.append(arry2)

# print(mainArray,costArray)

for test in range(0,len(mainArray)):
    for element in mainArray[test]:
        if element[2]<= costArray[test]:
            