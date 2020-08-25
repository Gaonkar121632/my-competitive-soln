stringLen=input()
string=input()

devicers=[2,3,5,7,11,13,17,19,23,29]

mtrx=[[],[]]
for x,i in enumerate(string):
    mtrx[0].append(i)
    mtrx[1].append(int(x))

print(mtrx)
# while True:
        
    