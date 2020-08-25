testCase = int(input())
allInputs = []
for ele in range(0, testCase):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    allInputs.append([arr1, arr2])


def findValTwo(arr, indx,lowBound):
    i = 0
    # j=0
    flag = True
    while flag:
        i += 1
        if (indx+i)<len(arr) and arr[indx+i] != (indx+i)+1:
            return indx+1
        elif (indx-i)>lowBound and arr[indx-i] != (indx-i)+1:
            return indx-1
        if (indx+i)>=len(arr) and (indx-i)<=lowBound:
            return -1



for sample in allInputs:
    allEle = sample[1]
    allRsults = []
    sortedArr=sorted(allEle)
    count=0
    for indx in range(0, len(sample[1])):

        if indx < len(sample[1]) and allEle[indx] != (indx+1):
            curIndx, valThree = indx, allEle[indx]
            twoIndx=valThree-1
            valTwo = allEle[twoIndx]
            indxOfValThree = allEle.index(curIndx+1)
            valOne = allEle[indxOfValThree]
            if valOne == valTwo:
                twoIndx=findValTwo(allEle,indxOfValThree,curIndx)
                valTwo=allEle[twoIndx]
                # print(valTwo)
                if twoIndx>-1:
                    count+=1
                    allRsults.append([indx+1, twoIndx+1, indxOfValThree+1])
                else:
                    break
                
                # allRsults = []
                # break
            else:
                count+=1
                allRsults.append([indx+1, twoIndx+1, indxOfValThree+1])
                # print(valThree,valTwo,valOne)
            allEle[indx] = valOne
            allEle[twoIndx] = valThree
            allEle[indxOfValThree] = valTwo
        if sortedArr==allEle or count>=sample[0][1]:
            break
        # print(allEle)

    if allEle == sortedArr and len(allRsults) > 0:
        print(len(allRsults))
        for val in allRsults:
            print(' '.join(map(str, val)))
        print(allEle)
    else:
        print(-1)
