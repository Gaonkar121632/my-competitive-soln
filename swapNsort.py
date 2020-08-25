import copy 

userInputs = []
testCases = int(input())
for x in range(0, testCases):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    userInputs.append([arr1, arr2])

for sample in userInputs:
    k=sample[0][1]
    arr=sample[1]
    Flag="yes"
    previous=[]
    swap=999
    while swap!=0:
        swap=0            
        for i in range(0,(sample[0][0]-k)):
            if (i+k)<len(arr) and arr[i]>arr[i+k]:
                temp=arr[i]
                arr[i]=arr[i+k]
                arr[i+k]=temp   
                swap+=1

    for i in range(1,sample[0][0]):
        if arr[i-1]>arr[i]:
            Flag='no'
            break
    
    print(Flag)
    
    