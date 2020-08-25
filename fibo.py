userInputs=[]
testCases=int(input())
for x in range(0,testCases):
    userInputs.append(int(input()))
    

pattern=[0 , 1 , 1 , 2 , 3 , 5 , 8 , 3 , 1 , 4 , 5 , 9 , 4 , 3 , 7 , 0 , 7 , 7 , 4 , 1 , 5 , 6 , 1 , 7 , 8 , 5 , 3 , 8 , 1 , 9 , 0 , 9 , 9 , 8 , 7 , 5 , 2 , 7 , 9 , 6 , 5 , 1 , 6 , 7 , 3 , 0 , 3 , 3 , 6 , 9 , 5 , 4 , 9 , 3 , 2 , 5 , 7 , 2 , 9 , 1]


def elemenateOdd(sampleArray):
    if len(sampleArray)>1:
        sampleArray=sampleArray[1::2]
        elemenateOdd(sampleArray)
    else:
         print(sampleArray[0])
         return


for inpt in userInputs:
    if inpt<60:
        sample= pattern[0:inpt]
        elemenateOdd(sample)
    else:
        multipuls=int(inpt/60)
        remider=int(inpt%60)
        sample=pattern*multipuls+pattern[0:remider]
        elemenateOdd(sample)

