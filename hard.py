testCases=int(input())
allTestcase= list(map(int, input().split()))

flag="easy"
for x in allTestcase:
    if x==1:
        flag="hard"
        break
print(flag)