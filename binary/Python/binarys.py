def binary_search(arr, searchingFor):
	length = len(arr)
	midNum = int(round(length/2))
	foundNum = False
	place = 0
	while (foundNum == False):
		print(arr)
		midNum = int(round(length/2))
		if arr[midNum] == searchingFor:
			foundNum = True
			return arr[midNum], place
		elif arr[midNum] < searchingFor:
			newArr = []
			for i in range(midNum, length):
				newArr.append(arr[i])
			arr = newArr.copy()
			length = length - midNum
			place += length+1
		elif arr[midNum] > searchingFor:
			newArr = []
			for i in range(midNum):
				newArr.append(arr[i])
			arr = newArr.copy()
			asd = length
			length = midNum
			place += asd


arr = [1, 3, 4, 5, 6, 7, 9]
a, b = binary_search(arr, int(input()))
print("Printed:",a, "Place:", b)
