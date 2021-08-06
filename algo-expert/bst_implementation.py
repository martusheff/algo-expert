"""
Description:

Implementation of a simple Binary Search Tree in Python.
Our Binary Search Tree  method allows for insertion and search on an instantiated BST.

Not part of AlgoExperts program, this will serve as a point of reference in studying.
"""


class Node: # Node (or the Value) of a position in a Tree.
	def __init__(self, data=None): # Initializes an empty Node when called by default.
		self.data = data # "data" passed in through constructor is set as an attribute of Node. (Nodes Value)
		self.left = None # self.left/self.right are routes for following methods to act upon a Node, and are not set here.
		self.right = None

class BST: # Binary Search Tree.
	def __init__(self):
		self.root = None # When a BST is created, attribute root is created with no value.

	def insert(self, data):
		if self.root is None: # Sets first passed value as root to a newly created BST.
			self.root = Node(data) # the root is equal to Node(data) where Node(data) is changed from "None" to passed "data"
		else:
			self._insert(data, self.root) # If root already exists, a recursive insertion method is called.

	def _insert(self, data, cur_node): # Takes in the initial data value trying to be inserted, as well as the current node.
		if data < cur_node.data: # If the data value being inserted is less than the current node value, we will try to set it to "node.left"
			if cur_node.left is None: 	# If node.left has not yet been assigned a value/created, it will finally create a Node(data) 
										# where data is the original data value trying to be passed in the initial insert method.
				cur_node.left = Node(data)
			else:
				self._insert(data, cur_node.left) # If node.left has already been assigned a value, "_insert()"" will be recursively called until
													# there is no longer a value assigned to node.left or it is equal to it.

		elif data > cur_node.data: # Same applied in this instance, except data larger than the current node will be set to node.right
			if cur_node.right is None:
				cur_node.right = Node(data)
			else:
				self._insert(data, cur_node.right)

		else:
			print("Value is already in binary search tree.") # If the data is not less than or greater than the current node value,
														# the value must then already be in the tree. This tells the user this information.

	def find(self, data): # Finding a value is similar to inserting a value, but the tree is only accessed and not altered.
		if self.root: # If the tree has a root node then... 
			is_found = self._find(data, self.root) # A recursive search method is implemented taking the parameters of the passed data value
			if is_found:							# and the root of the Tree.
				return True # If the recursive search returns True, find returns True, indicating that the value exists in the tree
			return False # if not, then the value is not in the tree and find() returns false.

		else:
			return None # if self.root does not exist then there is not data to look through. returns None.

	def _find(self, data, cur_node): # Recursive search method.
		if data > cur_node.data and cur_node.right: # if the passed data value is greater than the cur_node ((AND)) cur_node.right exists,
													# return the recursive search of updated inputs where _find() takes in the originally passed data
													# and the next node to the right (which in the next iteration becomes the cur_node).
			return self._find(data, cur_node.right)
		elif data < cur_node.data and cur_node.left:# same as above for values less than the cur data node, and to the left respectfully
			return self._find(data, cur_node.left)
		if data == cur_node.data: # if the originally passed data is (finally) equal to the cur_node, return True, indicating it exists within the tree
			return True



# Example of Use
bst = BST()

bst.insert(10)
bst.insert(10)
bst.insert(1993)

print(bst.find(5))
print(bst.find(4444))
print(bst.find(1993))
