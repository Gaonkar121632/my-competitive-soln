import random
operation = 1000
Trange = 1000
seqArr = []

for x in range(0, Trange):
    seqArr.append(x+1)

print(seqArr)
for val in range(0, operation):
    radomList = random.sample(range(0, Trange), 3)
    print(radomList)
    valOne = seqArr[radomList[0]]
    valTwo = seqArr[radomList[1]]
    valTh = seqArr[radomList[2]]

    seqArr[radomList[0]] = valTwo
    seqArr[radomList[1]] = valTh
    seqArr[radomList[2]] = valOne
print(' '.join(map(str, seqArr)))