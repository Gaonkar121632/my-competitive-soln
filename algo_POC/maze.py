from collections import deque

import numpy as geek 

sample=[
    [0,0,0,0],
    [0,1,0,1],
    [0,1,1,1],
    [0,0,0,0]
    ]
visited=geek.empty([4, 4])
visited.fill(0)

s=[0,0]
d=[len(sample)-1,len(sample[0])-1]
print(d)

def isValid(x,y):
    return (x>=0 and x<len(sample)) and (y>=0 and y<len(sample[0]))

axis=[[0,-1,0,1],[-1,0,1,0]]
def bfs(sample):
    q=deque([])
    q.append(s)
    while q:
        print(visited)
        current = q.popleft()
        if current[0]!=d[0] or current[1]!=d[1]:
            for i in range(0,4):
                x=current[0]+axis[0][i]
                y=current[1]+axis[1][i]

                if isValid(x,y) and sample[x][y]==0 and visited[x][y]==0:
                    # print(x,y)
                    visited[x][y]=1
                    q.append([x,y])
        else:
            break
bfs(sample)