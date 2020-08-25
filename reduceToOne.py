# filteredInput=[3,2,4]
testCase = input()
filteredInput=[]
for n in range(0,int(testCase)):
    ip = input()
    filteredInput.append(int(ip))

def calculate(x,y):
    return x+y+(x*y)

def operate(sample):
    while len(sample)>1: 
        var1=sample[0]
        var2=sample[len(sample)-1]
        indx=len(sample)-1
        sample.append(calculate(var1,var2))
        del sample[indx]
        del sample[0]
        # operate(sample)
    return sample[0]
        
    

for x in filteredInput:
    testArray=[]
    for ele in range(1,x+1):
        testArray.append(ele)
    print(operate(testArray))
    

         