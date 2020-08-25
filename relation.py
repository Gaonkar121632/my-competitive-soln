allInputs=int(input())
allData=[]
for x in range(0,allInputs):
	tempArr=list(map(int,input().split()))
	if tempArr[0]==tempArr[1]:
		allData.append("=")
	elif tempArr[0]>tempArr[1]:
		allData.append(">")
	elif tempArr[0]<tempArr[1]:
		allData.append("<")
for x in allData:
	print(x)
