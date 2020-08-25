allInputs=[]
test=int(input())
for x in range(0,test):
    dummy=int(input())
    allInputs.append(dummy)

for x in allInputs:
    if x%2==0:
        print(int((x/2))-1)
    else:
        print(int(x/2))