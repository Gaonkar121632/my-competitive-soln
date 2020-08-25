# testCase = input()
allInputs = [[0,1,0]]
# for x in range(0,int(testCase)):
#     dummpy=input()
#     arr1 = list(map(int, input().split()))
#     allInputs.append(arr1)

for sample in allInputs:
    totalProfit=0
    while len(sample):
        print(sample)
        maxOne=max(sample)
        totalProfit+=0 if maxOne<0 else maxOne
        sample.remove(maxOne)
        sample=list(filter((0).__ne__, sample))
        sample = [x - 1 for x in sample]
    print(totalProfit)