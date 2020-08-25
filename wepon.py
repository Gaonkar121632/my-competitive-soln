allTest=int(input())
allInputs=[]
for x in range(0,allTest):
    temp=int(input())
    tempArr=[]
    for y in range(0,temp):
        z=input()
        tempArr.append(z)
    allInputs.append(tempArr)


for sample in allInputs:
    midResult=sample[0]
    for value in range(1,len(sample)):
        l = [ord(a) ^ ord(b) for a,b in zip(midResult,sample[value])]
        midResult=''.join(str(x) for x in l)
    print(str(midResult).count('1'))