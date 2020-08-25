from itertools import combinations
import numpy
import math


# testCase = input()
allInputs = []
# for x in range(0,int(testCase)):
#     dummpy=input()
#     arr1 = list(map(int, input().split()))
#     allInputs.append(arr1)

# for x in range(0,100):


def prod(inputArr):
    prod=1
    for x in inputArr:
        prod=round(prod*x,1)
    return prod    
allInputs.append(list(range(0, 1000)))
# "%.2f" % round(, 2)

for L in allInputs:
    count = 0
    size = 0
    # L=[round(math.sqrt(x),2) for x in L]
    for w in range(1, len(L)+1):

        for i in range(len(L)-w+1):
            # print(numpy.prod(L[i:i+w]))
            # print(L)
            # total = numpy.prod(L[i:i+w])
            total = prod(L[i:i+w])
            
            # print(L[i:i+w])
            # total=round(total, 2)
            # print(total)
            pSquare = math.ceil(math.sqrt(total))
            q = (pSquare*pSquare)-total
            # print("q-->",q,"-->",(pSquare*pSquare),"-",total)
            if q>=0:
                q = math.sqrt(q)
                if q == math.floor(q):
                    count += 1
    print(count)
