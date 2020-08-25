testCase = int(input())
allInputs = []
for ele in range(0, testCase):
    arr1 = list(map(int, input().split()))
    allInputs.append(arr1)


for sample in allInputs:
    result = sample[0] | sample[1]
    if result>sample[3]:
        maxRes,indx=0,0
        for x in range(sample[2],sample[3]+1):
            res=(sample[0]&x)*(sample[1]&x)
            if maxRes<res:
                maxRes=res
                indx=x
        print(indx)
    elif result>sample[2]:
        print(result)

        