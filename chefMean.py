import numpy as np 


testCase = input()
allInputs = []
for x in range(0,int(testCase)):
    temp=input()
    arr1 = list(map(int, input().split()))
    allInputs.append(arr1)

# testCase=[[1,2,3,4,5,6,7,8,9],[5,4,3,6],[10000,10000,10000,10000,10000,10000]]

for test in allInputs:
    mean=np.mean(test)
    if mean in test:
        print(test.index(mean)+1)
    else :
        print('Impossible')




