testCase=int(input())
allInputs=[]

def evenOrOdd(XorList):
    # print(XorList)
    even,odd=0,0
    for ele  in XorList:
        num = ele
        Res=0
        while num > 0 :
            # print("num",num)
            current = int(num) & 1
            Res = Res + current
            num = (num - current) / 2
        if Res%2==0:
            even=even+1
        else :
            odd=odd+1
    return {
        "even":even,
        "odd":odd
    }
for x in range(0,testCase):
    tempArr=[]
    numberP = list(map(int, input().split()))[1]
    sampleArr=list(map(int, input().split()))
    itemsArr=[]
    for item in range(0,numberP):
        itemsArr.append(int(input()))
    tempArr.append(sampleArr)
    tempArr.append(itemsArr)
    allInputs.append(tempArr)

# print(allInputs)

for item in allInputs:
    for element in item[1]:
        xorList=[ sample^element for sample in item[0]]
        evenOdd=evenOrOdd(xorList)
        print(evenOdd["even"],evenOdd["odd"])