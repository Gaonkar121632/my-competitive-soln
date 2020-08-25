def binarySearch(arr,item):
	low=0
	high=len(arr)-1
	while low<=high:
		mid=int((low+high)/2)
		guess=arr[mid]
		if guess==item:
			return  mid
		if item>guess:
			low=mid+1
		else:
			high=mid-1
	return None

arr=[1,2,3,4,5]
print(binarySearch(arr,40))
