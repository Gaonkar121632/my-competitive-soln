testCase = int(input())
allInputs = []
for ele in range(0, testCase):
    dumm=input()
    arr1 = list(map(int, input().split()))
    allInputs.append(arr1)

# print(allInputs)
for sample in allInputs:
    flag=True
    visited=[[],[],[]]
    for value in sample:
        if value in visited[0]:
            found=visited[0].index(value)
            if visited[2][found]:
                flag=False
                break
            else:
                visited[1][found]+=1  
        else:
            if len(visited[0])>0:
                visited[2][len(visited[0])-1]=True
                same=visited[1][len(visited[0])-1]
                if same in visited[1][0:len(visited[0])-1]:
                    flag=False
                    break
                else:
                    visited[0].append(value)
                    visited[1].append(1)
                    visited[2].append(False)

            else:
                visited[0].append(value)
                visited[1].append(1)
                visited[2].append(False)
    
    same=visited[1][len(visited[0])-1]
    if same in visited[1][0:len(visited[0])-1]:
        flag=False
        

    if flag:
        print("YES")
    else:
        print("NO")
        