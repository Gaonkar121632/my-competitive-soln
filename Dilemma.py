testCase = input()
inputValue = []
for x in range(0,int(testCase)):
    arr1 = input()
    inputValue.append(arr1)


for value in inputValue:
    stringLength=len(value)
    zeros=value.count('0')
    if stringLength%2==0 and zeros%2!=0 :
        print("WIN")
    
    elif stringLength%2!=0 and zeros%2==0 :
        print("WIN")
    else:
        print("LOSE")
