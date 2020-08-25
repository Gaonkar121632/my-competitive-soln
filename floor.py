allInput=[['1', '1', '1', '1', '1'], ['1', '0', '0', '0', '1'], ['1', '0', '0', '0', '0'], ['1', '1', '1', '0', '1']]


       
    
def findFloor(x,y):
    allInput[x][y]=-1
    # if x<len(allInput) and y<len(allInput[x])-1:  
       
    if y+1<len(allInput[x]) and allInput[x][y+1]=='1' :
        findFloor(x,y+1)
                
    if x+1<len(allInput) and allInput[x+1][y]=='1' :
        findFloor(x+1,y)

count=0
for idx,ele in enumerate(allInput):
    while '1' in ele:
        count=count+1
        findFloor(idx,ele.index('1'))
print(count)

