import math  

allInputs=[{
    "black":[1,4],
    "colors":[[4,4,2,0,8,1],[10,1,3,1],[1,3,9,5]],
    "red":[4,4,2,0,8,1],
    "green":[10,1,3,1],
    "blue":[1,3,9,5]
}]


def findDistance(cor1,cor2):
    corResult=pow((cor2[0]-cor1[0]),2)+pow((cor2[1]-cor1[1]),2)
    print(math.sqrt(corResult))
    return math.sqrt(corResult)

for testCase in allInputs:
    # for sample in testCase["colors"]:
    #     minimum=999
    #     while len(sample):
    #         arr=[]
    #         arr.append(sample.pop())
    #         arr.append(sample.pop())
    #         findDistance(testCase["black"],arr[::-1])
            # print(arr[::-1])
    round=0
    if round==0:
        pass
    elif round==1:
        pass
    elif round==2:
        