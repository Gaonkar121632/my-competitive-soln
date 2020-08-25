# allInputs=[[[2,4,1,11,1,6,13,20,27],[8,1]]]

testCase = input()
allInputs=[]
for x in range(0,int(testCase)):
    temparray=[]
    # for j in range(0,int(y)):
    arr1 = list(map(int, input().split()))
    arr2= list(map(int, input().split()))
    temparray.append(arr2)
    temparray.append(arr1)
    # print(temparray)
    allInputs.append(temparray)



for sample in allInputs:
    # sample1=[x+sample[1][1] for x in sample[0]]
    count=0
    # for x in sample1:
    #     if x%7==0:
    #         count=count+1
    # print(count)
    for ele in sample[0]:
        if ((ele+sample[1][1])%7)==0 :
            count=count+1
    print(count)
            