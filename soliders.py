# input_x=[[[5,4,5,4,5,4,5],[3,2,4,7,2,5,9]]]
testCase = input()
input_x=[]
for x in range(0,int(testCase)):
    temparray=[]
    y=input()
    # for j in range(0,int(y)):
    arr1 = list(map(int, input().split()))
    arr2= list(map(int, input().split()))
    temparray.append(arr1)
    temparray.append(arr2)
    # print(temparray)
    input_x.append(temparray)

# print(input_x)

def check_defence(main_array):
    high_defence=-1
   
    # result=main_array[1][i]-(main_array[0][i-1]+main_array[0][i+1])
    for i in range(0,len(main_array[0])):
        left=i-1
        right=i+1
        if i==0:
            left=len(main_array[0])-1
        if i==(len(main_array[0])-1):
            right=0

        result=main_array[1][i]-(main_array[0][left]+main_array[0][right])
        if result>0:
            if high_defence<main_array[1][i]:
                high_defence=main_array[1][i]
    print(high_defence)
    

for inputArray in input_x:
    check_defence(inputArray)
