import math

testCase = int(input())
allInputs = []
for ele in range(0, testCase):
    arr1 = input()
    allInputs.append(arr1)


for sample in allInputs:
    # print(len(sample))
    half=len(sample)//2
    otherHalf=math.ceil(half/2)
    
    # print(sample[0:otherHalf],otherHalf)
    # print(sample[otherHalf:otherHalf*2])
    print(sample[len(sample)-otherHalf:len(sample)],sample[half-1:(half+otherHalf)-1],half,half+otherHalf)
    if sample[0:otherHalf]==sample[otherHalf:otherHalf*2]:
        # secondSet=len(sample)-otherHalf*2
        print(1)
    elif sample[len(sample)-otherHalf:len(sample)]==sample[half-1:(half+otherHalf)-1]:
        print(1)
    else:
        print(0)