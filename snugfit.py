# input_x=[[[10,10,10,20,20,20],3]]
testCase = input()
input_x=[]
for x in range(0,int(testCase)):
    temparray=[]
    y=int(input())
    arr1 = list(map(int, input().split()))
    arr2= list(map(int, input().split()))
    input_x.append([sorted(arr1+arr2),y])


for sample in input_x:
    sum=0
    for ele in range(0,sample[1]):
        sum=sum+sample[0][ele]
        # print(sample[0][ele])
    print(sum)
