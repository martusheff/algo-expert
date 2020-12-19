def findClosestValueInBst(tree, target):
	findClosest(tree, target, tree.value)

def findClosest(tree, target, closest):
	closest = abs(tree.value - target)
	while tree.left is not None:
		if findClosest()


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None