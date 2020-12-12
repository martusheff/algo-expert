# Given Data
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10


# Simple Solution (nested for loops)
# T: O(n^2) S: O(1)
def twoNumberSumV1(array, targetSum):
	arr = []
	for x in array: 						# Iterates through array
		for y in array:						# Iterates through array for every value in array
			if (array.index(x) != array.index(y)) and x + y == targetSum: 	# Checks if vals add up to targetSum
	  			arr = [x,y]
	return arr



# Better Solution (hash map)
# T: O(n) S: O(n)
def twoNumberSumV2(array, targetSum):
	numHash = {}							# Dictionary named numHash
	for i in array:							
		potentialMatch = targetSum - i		
		if potentialMatch in numHash:		# If needed # is in numHash, accessed in O(1) time
			return [potentialMatch, i]
		else:								
			numHash[i] = True				# Add array[i] to numHash as Key w/ Value of True
	return []
		

# Best Solution (sorted)
# T: O(nlog(n)) S: O(1)
def twoNumberSumV3(array, targetSum):
	array.sort()							# Sorts in O(nlog(n)) time
	first = 0								# Leftmost index/boundary of array
	last = len(array) - 1					# Rightmost index/boundary of array

	while first < last:
		if (array[first] + array[last]) == targetSum:
			return[array[first],array[last]]
		elif (array[first] + array[last]) < targetSum: # If sum is short of target, remove smallest val.
			first += 1
		elif (array[first] + array[last]) > targetSum: # If sum is high to target, remove largest val.
			last -= 1

	return[]



# Test Case
print("Solution One:	" + str(twoNumberSumV1(array, targetSum)))
print("Solution Two:	" + str(twoNumberSumV2(array, targetSum)))
print("Solution Three:	" + str(twoNumberSumV3(array, targetSum)))


""" Description:
	
	In twoNumberSum, we are trying to find two values in a given array that add up to
	a given targetSum.
						"""


