testCase = input()
input_x=[]
for x in range(0,int(testCase)):
    temparray=[]
    arr1 = list(map(int, input().split()))
    arr2= list(map(int, input().split()))
    total=sum(arr2)
    input_x.append([total,arr1[1]])

for ele in input_x:
    result=ele[0]%ele[1]
    print(result)