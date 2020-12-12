# Given Data
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

# Solution:
# T: O(n) S: O(1)	
def isMonotonic(array):
	isNonIncreasing = True		# assumes array is non increasing
	isNonDecreasing = True		# assumes array is non decreasing

	for i in range(1, len(array)):	# for index range starting at 1
		if array[i] < array[i-1]:	# if index is less than the previous index, array is decreasing
			isNonDecreasing = False	
		if array[i] > array[i-1]:	# if index is greater than the previous index, array is increasing
			isNonIncreasing = False

	return isNonIncreasing or isNonDecreasing	# returns true if at least one assumptions is held, false if not

# Testing Data
print(isMonotonic(array))