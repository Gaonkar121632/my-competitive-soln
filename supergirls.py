allInputs=[]
dummy=input()
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
allInputs.append([arr1,arr2])

for sample in allInputs:
    mini=float("inf")
    for i in range(0,len(sample[0])):
        res=sample[1][i]/sample[0][i]
        mini=res if res<mini else mini
    print(int(mini))