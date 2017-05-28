class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST(object):
	def __init__(self, root):
		self.root = Node(root)

	def insert(self, new_val):
		self.insert_helper(self.root, new_val)

	def insert_helper(self, current, new_val):
		if current.value < new_val:
			if current.right:
				self.insert_helper(current.right, new_val)
			else:
				current.right = Node(new_val)
		else:
			if current.left:
				self.insert_helper(current.left, new_val)
			else:
				current.left = Node(new_val)

	def search(self, val):
		self.search_helper(self.root, val)

	def search_helper(self, current, val):
		if current:
			if current.value == val:
				return True
			elif current.value < val:
				self.search_helper(current.right, val)
			else:
				self.search_helper(current.left, val)

		return False

	def preOrder(self, current):
		if current:
			print(current.value, end=" ")
			preOrder(current.left)
			preOrder(current.right)

	def inOrder(self, current):
		if current:
			self.inOrder(current.left)
			print(current.value, end=" ")
			self.inOrder(current.right)

	def postOrder(self, current):
		if current:
			postOrder(current.left)
			postOrder(current.right)
			print(current.value, end=" ")

	def height(self, current):
		if current == None:
			return -1
		else:
			return 1 + max(height(current.left), height(current.right))



