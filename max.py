inputValue=[]
tesCase=int(input())

for value in range(0,tesCase):
    tesArray=[]
    temp1=list(map(int,input().split()))
    scores=list(map(int,input().split()))
    query=list(map(int,input().split()))
    tesArray.append(scores)
    tesArray.append(query)
    inputValue.append(tesArray)




for value in inputValue:
    sample=value[0]
    for x in value[1]:
        tempSample=sample[0:x]
        # tempSample.sort()
        # print(tempSample[len(tempSample)-1])
        print(max(tempSample))
