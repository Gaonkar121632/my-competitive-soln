initial='xyz'
goal="xzyxz"
count=0

def Sorting(lst): 
    lst.sort(key=len,reverse=True) 
    return lst 

allSubString=list(initial[i:j+1] for i in range (len(initial)) for j in range(i,len(initial)))
allSubString=Sorting(allSubString)
for ele in allSubString:
    while goal.find(ele) is not -1:
        count=count+1
        goal.replace(ele,"",1)