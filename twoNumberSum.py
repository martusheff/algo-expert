array = [(x * 2) for x in range(10)]

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):
	arr = []
	for x in array:
		for y in array:
			if (array.index(x) != array.index(y)) and x + y == targetSum:
	  			arr = [x,y]
	  			return arr

print(twoNumberSum(array, targetSum))
