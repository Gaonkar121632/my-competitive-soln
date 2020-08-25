testCase = input()
inputValue = []
for x in range(0,int(testCase)):
    tempInput=int(input());
    tempValue=[]
    for y in range(0,2):
        arr1 = list(map(int, input().split()))
        tempValue.append(arr1)
    inputValue.append(tempValue)

    
for testValue in inputValue:
    maxValue=0
    for indx,value in enumerate(testValue[0]):
        result=(value*20)-(testValue[1][indx]*10)
        maxValue=result if result>maxValue else maxValue
    print(maxValue)