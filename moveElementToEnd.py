def moveElementToEnd(array, toMove):
	x = len(array) - 1

	i = 0
	for num in array:
		if (num == toMove) and (i < x):
			array.append(array.pop(array.index(num)))
			i += 1
	return array
