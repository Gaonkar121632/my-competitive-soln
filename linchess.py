allInputs = []
totalTest = int(input())
for i in range(0, totalTest):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    allInputs.append([arr1, arr2])

# print(allInputs)
for sample in allInputs:
    count = 0

    for x in sample[1]:
        # print(x%sample[0][1])
        if(sample[0][1] % x == 0):
            count += ((sample[0][1]-x)/x)

    if count > 0:
        print(int(count))
    else:
        print(-1)
