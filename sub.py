import itertools

testCase=[[[0,2,1,2,0,4,5,10,8,0,9,1,2,6,7,8,15,96,90,1,0],[5]]]
# test = input()
# testCase = []
# for x in range(0,int(test)):
#     tempInput=[]
#     arr1 = list(map(int, input().split()))
#     arr2 = list(map(int, input().split()))    

#     tempInput.append(arr2)
#     tempInput.append([arr1[1]])
#     testCase.append(tempInput)

# print(testCase)

for sample in testCase:
    sample[0].sort()
    index=sample[1][0]
    newSample=sample[0][0:index]
    # print(newSample,sample[0])
    while len(sample[0])>index and newSample[len(newSample)-1]==sample[0][index]:
        newSample.append(sample[0][index])
        index=index+1
    combination =list(itertools.combinations(list(newSample), sample[1][0]))
    print(combination)
    # minSum=999
    # count=0
    # for element in combination:
    #     if sum(element)<minSum:
    #         minSum=sum(element)
    #         count=1
    #     elif sum(element)==minSum:
    #         count=count+1
    # print(count)


        