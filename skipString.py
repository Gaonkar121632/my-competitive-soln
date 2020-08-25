userInputs = []
testCases = int(input())
for x in range(0, testCases):
    dummy = int(input()) 
    val=list(map(int, input().split()))
    userInputs.append(val)


for sample in userInputs:
    total=0
    for x in range(1,len(sample)):
        result=abs(sample[x-1]-sample[x])
        total+=result-1
    print(total)