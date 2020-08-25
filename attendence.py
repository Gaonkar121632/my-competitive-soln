# testCase = int(input())
inputArr=[]
for x in range(0, testCase):
    temp=input()
    data=input()
    inputArr.append(data)

# inputArr=['PAAPP',"PAPPAPPAPPAPAPAPAPPAPAPPAPAPA","APAPPPAPAPAPAPAPAPPAPAPAPAPAA","AAAPPPAPAPAP","PA",'AAPPPPP',"PPPAAPPPPP","APAPAPAPAP","AAAAAAAAA"]
for attendence in inputArr:
    minCount=0
    flag=False
    toataP=attendence.count('P')
    toataA=attendence.count('A')
   
    # print("toataP=>",toataP,"len=>",len(attendence),"totalA=>",toataA)
    for i in range(2,(len(attendence)-2)):
        if i==2 and (toataP/len(attendence)) >=0.75:
            print(0)
            flag=True
            break
        if attendence[i] == 'A' and (attendence[i-1]=="P" or attendence[i-2]=="P") and (attendence[i+1]=="P" or attendence[i+2]=="P"):
            minCount= minCount+1
            if (toataP+minCount)/len(attendence)>=0.75:
                print(minCount)
                flag=True
                break
    if flag== False:
        print(-1)
            