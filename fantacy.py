userInputs = []
testCases = int(input())
for x in range(0, testCases):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
    userInputs.append([arr1, arr2, arr3])


for sample in userInputs:
    total = sample[0][1]
    minOne = float("inf")
    minTwo = float("inf")
    for x in range(0, sample[0][0]):
        if sample[2][x] == 0 and sample[1][x]<minOne:
            minOne=sample[1][x]
        elif sample[2][x] == 1 and sample[1][x]<minTwo:
            minTwo=sample[1][x]
    if ((minOne+minTwo)+total)<=100:
        print("yes")
    else:
        print("no")
