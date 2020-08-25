dpArr=[0]*100
dpArr[0]=0
def MinStep(num):
    for i in range(2,num+1):
        minVal=dpArr[(i-1)-1]
        if i%2==0 and dpArr[(i//2)-1]<minVal:
            minVal=dpArr[(i//2)-1]
        elif i%3==0 and dpArr[(i//3)-1]<minVal:
            minVal=dpArr[(i//2)-1]
        dpArr[i-1]=minVal+1
    print(dpArr[num-1])

MinStep(8)
