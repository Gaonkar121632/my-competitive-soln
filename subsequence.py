import itertools

testCase=[[[0,2,1,2,0,1,4,9,0],[3]]]


def takeSecond(elem):
    return elem[1]

# for sample in testCase:
#     sample[0].sort()
#     print(sample)
#     result={
#         "Sum":9999,
#         "freeq":0
#     }
#     for indx,value in enumerate(sample[0]):
#         target=value
#         tempArray=sample[0][indx+1:]
#         # print(tempArray)
#         for i,subValue in enumerate(tempArray):
#             # print(sample[1][0])
#             arraySum=sum(tempArray[i:(i+sample[1][0])-1])
#             print("sum",arraySum)
#             sumValue=target+subValue
#             # print(subValue,result["Sum"])
#             if subValue<=result["Sum"]:
#                 result['Sum']=sumValue
#                 result["freeq"]=result["freeq"]+1
#     print(result["freeq"])


# list(itertools.combinations((1, 2, 3), 2)) 
for sample in testCase:
    sample[0].sort()
    print(sample)
    result={
        "Sum":9999,
        "freeq":0
    }
    # for value in enumerate(sample[0]):
    x=list(itertools.combinations(list(sample[0]), 2)).sort(key=takeSecond)
    x.sort(key=takeSecond)
    print(x)


        