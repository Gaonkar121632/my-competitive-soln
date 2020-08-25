allInputs={}
# allInputs["ingrediant"]=[3,1,8,2,4,7]
allInputs["sample"]=[]
dummy=input()
allInputs["ingrediant"]=list(map(int,input().split()))
tesCase=int(input())
for x in range(0,tesCase):
    arr=list(map(int,input().split()))
    allInputs["sample"].append(arr)
    
# print(allInputs)
for sample in allInputs["sample"]:
    # L=sample[0]-1
    # R=sample[1]
    Q=sample[2]
    subIngrediant=allInputs["ingrediant"][sample[0]-1:sample[1]]
    if sum(subIngrediant)<Q:
        print(-1)
    else:
        subIngrediant.sort()
        result=0
        Flag=True
        for x in subIngrediant:
            result=result+x
            if result>=Q:
                print(result)
                Flag=False
                break
        
        if Flag:
            print(-1)