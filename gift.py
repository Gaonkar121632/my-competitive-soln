import math
# counts,allInputs,counter=[8,4],[1,2,8],0
counts=list(map(int, input().split()))
allInputs=list(map(int, input().split()))
counter=0

for ele in range(0,counts[0]):
    if not (ele+1) in allInputs and (ele in allInputs or (ele+2) in allInputs):
        counter=counter+1
        # print(ele+1)
x=math.factorial(counter)
print(x%1000000007)