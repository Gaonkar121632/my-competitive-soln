stringLen=int(input())
allSqr=[1]
for x in range(1,1019):
    allSqr.append(2*allSqr[x-1])

allInputs=[]
for x in range(0,stringLen):
    allInputs.append(int(input()))
    
# print(allSqr[len(allSqr)-1])

def findOne(l,r,val):
    for x in allSqr:
        if x>val:
            break
        mini=x
    return mini
    # if r>=l:
    #     mid=l+(r-l)//2
    #     if (allSqr[mid]>val and allSqr[mid-1]<val) or allSqr[mid]==val:
    #         if allSqr[mid]==val:
    #             return allSqr[mid]
    #         else:
    #             return allSqr[mid-1]
    #     elif allSqr[mid]>val:
    #         return findOne(l,mid-1,val)
    #     else:
    #         return findOne(mid+1,r,val)
    

def compute(mini,value,count):
    # print(value,mini)
    result=value-mini
    if(result<1):
        return count
    else:
        mini=findOne(0,len(allSqr)-1,result)
        return compute(mini,result,count+1)
    

for value in allInputs:
    result=findOne(0,len(allSqr)-1,value)  
     
    final=compute(result,value,1)
    print(final)
    