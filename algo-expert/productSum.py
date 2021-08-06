array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def productSum(array):
	res = 0
   	for x in array:
		if type(x) == int:
			res += x
		if type(x) == list:
			productSum(array, mult)
			res += productSum
	return res


print(productSum(array))