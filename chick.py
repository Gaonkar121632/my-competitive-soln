# allInputs=[[2,4,6]]
allInputs=[]
test=int(input())
for x in range(0,test):
    dummy=input()
    arr1 = list(map(int, input().split()))
    allInputs.append(arr1)

for ele in allInputs:
    print(min(ele))