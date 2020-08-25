testCase = input()
allInputs = []
for x in range(0,int(testCase)):
    arr1 = list(map(int, input().split()))
    allInputs.append(arr1)


def computeMin(num):
    global minimum,flag,decimal,previosmin
    possibleCombo=[]
    duplicatemin=str(minimum)
    # flag=False
    for i in range(0, len(duplicatemin)):
        l = list(duplicatemin)
        del (l[i])
        result = ''.join(l)
        possibleCombo.append(int(result+str(decimal)))
    
    selectedMin=min(possibleCombo)
    if selectedMin<minimum:
        previosmin=minimum
        minimum=selectedMin
    else:
        previosmin=minimum
    
        

    
    
    


for element in allInputs:
    decimal=element[1]
    previosmin=999999999
    minimum=element[0]
    flag=True
    while flag:
        if previosmin==minimum :
            flag=False
        else:
            computeMin(minimum)
    print(minimum)
