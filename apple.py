# inputValue=[[4,2]]
import math  

testCase = input()
inputValue = []
for x in range(0,int(testCase)):
    arr1 = list(map(int, input().split()))
    inputValue.append(arr1)

def printDivisors(n) : 
    status='NO'
    i = 1
    while i <= math.sqrt(n[0]): 
        reminder=n[0] % i
        if ( reminder==0 and i !=n[1] and i != n[0] and i != 1 ) :  
            status='YES' 
        i = i + 1
    return status



for testCase in inputValue:
   print(printDivisors(testCase))