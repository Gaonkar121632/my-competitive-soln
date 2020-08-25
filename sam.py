# tesCase=[[2,3]]
tesCase=[]
allInput=int(input())
for x in range(0,allInput):
    dummy=input()
    arr=list(map(int,input().split()))
    tesCase.append(arr)


for sample in tesCase:
    # prod=1
    allSum=0
    prev=0
    for indx,val in enumerate(sample):
        if indx==0:
            prev=val
        else:
            prduct=prev*val
            allSum=allSum+prduct
            prev=prev+val
    print(allSum)