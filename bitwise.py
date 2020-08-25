testCase = int(input())
allInputs = []
for ele in range(0, testCase):
    arr1 = list(map(int, input().split()))
    allInputs.append(arr1)


# print(allInputs)
for sample in allInputs:
    ResultVal=sample[0]
    final=0
    for x in range(sample[2],sample[3]+1):
        result=(sample[0]&x)*(sample[1]&x)
        print("x",sample[0]&x,"y",sample[1]&x,"z",x)
        print(result)
