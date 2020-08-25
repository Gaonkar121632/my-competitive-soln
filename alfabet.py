alphabet={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
def lookup(n):
    return alphabet[n]

# allInputs=[[4,['a','b','b','c','a']]]
testCase=int(input())
allInputs=[]
for ele in range(0,testCase):
    tempArr=[]
    arr1 = list(map(int, input().split()))
    arr2 = list(input())
    tempArr.append(arr1[1])
    tempArr.append(arr2)
    allInputs.append(tempArr)

# print(allInputs)
for element in allInputs:
    target=element[0]
    numArr=list(map(lookup,element[1]))
    i,prevIndx,summ,flag,count,prev=0,0,0,True,0,0

    while prevIndx<len(numArr):
        if summ == target:
            count=count+1
            i=i+1
            summ=0
            prevIndx=prevIndx+1
            i=prevIndx
        elif summ<target:
            if i<len(numArr):
                summ=summ+numArr[i]
                i=i+1
            else:
                break
        elif summ>target:
            prevIndx=prevIndx+1
            i=prevIndx
            summ=0
    print(count)
            