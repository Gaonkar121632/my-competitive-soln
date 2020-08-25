import math

inputValue=[[[40,30,50],[30,0,51]],[[0],[10]]]

# testCase = input()
# inputValue = []
# for x in range(0,int(testCase)):
#     tempInput=int(input());
#     tempValue=[]
#     for y in range(0,2):
#         arr1 = list(map(int, input().split()))
#         tempValue.append(arr1)
#     inputValue.append(tempValue)
# print(allInputs)

for testValue in inputValue:
    Flag=True
    MAX_VAL=0
    mapValue={}
    sortedGoals=sorted(testValue[0],reverse=True) 
    # print(sortedGoals)
    for indx,value in enumerate(testValue[0]):
        mapValue[indx]=value;
    
    index=0
    while Flag:
        possibleForNext=((sortedGoals[index]-sortedGoals[index+1])*2)+1 if index<len(sortedGoals)-1 else math.inf
        indxOfValue=list(mapValue.keys())[list(mapValue.values()).index(sortedGoals[index])]
        if possibleForNext<testValue[1][indxOfValue]:
            MAX_VAL=(sortedGoals[index]*20)-(testValue[1][indxOfValue]*10)
            index=index+1
        else:
            temp_max=(sortedGoals[index]*20)-(testValue[1][indxOfValue]*10)
            MAX_VAL= MAX_VAL if MAX_VAL>temp_max else temp_max
            MAX_VAL=MAX_VAL if MAX_VAL>0 else 0
            Flag=False 
    print(MAX_VAL)  
