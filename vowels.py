def climbingLeaderboard(scores, alice):
    mylist = list(dict.fromkeys(scores))
    # foundd=0,num=0,final=[]
    final=[]
    duplicate=mylist
    # print(mylist)
    for item in alice:
        for ele in range(len(mylist),0,-1):
            if item>=scores[ele-1]:
                foundd=item
                num=scores[ele-1]
                break
        indexOf=mylist.index(num)
        if num <= foundd:
            final.append(num+1)
        elif num > foundd:
            final.append(num+2)

    return final

result=climbingLeaderboard([100,90,90,80,75,60],[50,65,77,90,102])
print(result)