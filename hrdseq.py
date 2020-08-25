alltest=int(input())
allInputs=[]
for x in range(0,alltest):
    temp=int(input())
    allInputs.append(temp)

for n in allInputs:
    sequence=['0']

    for x in range(1,n):
        currIndex=len(sequence)-1
        intial= sequence.pop()
        if intial in sequence :
            prevIndex=len(sequence) - 1 - sequence[::-1].index(intial)
            sequence.append(intial)
            sequence.append(str(currIndex-prevIndex))
            
        else :
                sequence.append(intial)
                sequence.append("0")

    print(sequence)
    print(sequence.count(sequence[len(sequence)-1]))   
