# Given Data
array = [1,1,1,1]
sequence = [1,1,1]

# My Attempt (Passes all Test Cases)
# T: O(n) S: O(n)
def isValidSubsequence(array, sequence):
	arr = []
	i = 0
	for x in array:
		if x == sequence[i]:
			arr.append(x)
			i += 1
			if i == (len(sequence)):
				break

	if arr == sequence:
		return True
	else:
		return False


# Test Methods
print(isValidSubsequence(array, sequence))