testCase=int(input())
inputValue=[]
for x in range(0,testCase):
    temp=input()
    Q=input()
    A=input()
    inputValue.append(Q)
    inputValue.append(A)

    
print(inputValue)
# inputValue=["DACA","AADD"]
i=0

while i<len(inputValue):
    print("ok")
    count=0
    j=0
    actualAns=inputValue[i]
    answered=inputValue[i+1]
    i=i+2
    # for indx,value in enumerate(actualAns):
    while j<len(actualAns):
        
        if actualAns[j]==answered[j]:
            count=count+1
        
        elif actualAns[j] !=answered[j] and answered[j] !="N" :
            j=j+1
        
        j=j+1
        
        
    print(count)


            
        


