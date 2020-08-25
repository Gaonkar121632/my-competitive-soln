testCase = input()
mainArray=[]
for x in range(0, int(testCase)):
    y = input()
    arry2=[]
    for target_list in range(0,int(y)):
        value=input()
        arry2.append(value)
    mainArray.append(arry2)
# mainArray = [['aaaa', 'aaxa', 'axaa'], ['asdfss']]

def compute_ingredients(array):
    count = 0
    thisset= set()
    value=array[0]
    for i in value:
        for ele in range(1,len(array)):
            if (i not in array[ele]):
                break
            elif(ele == (len(array)-1)):
                thisset.add(i)
    print(len(thisset))

for item in mainArray:
    compute_ingredients(item)