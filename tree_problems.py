class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def are_siblings(nodes, root):
	depth_charts = []
	for node in nodes:
		depth_charts.append(dfs(node, root))
	return depth_charts

def dfs(v1, root, path=None):
	if path is None:
		path = []
	if root is None:
		return
	elif root.val == v1 or dfs(v1, root.left, path) or dfs(v1, root.right, path):
		path.append(root.val)
	return path

def lca(root, n1, n2):
	if root is None:
		return None
	if root.val in [n1, n2]:
		return root.val
	left_val = lca(root.left, n1, n2)
	right_val = lca(root.right, n1, n2)
	if left_val is not None and right_val is not None:
		return root.val
	if left_val is None and right_val is None:
		return None
	if left_val is not None:
		return left_val
	else:
		return right_val


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
print(are_siblings([5, 4], root))

print(lca(root, 4, 5))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.right = Node(7)
print(lca(root, 5, 9))
print(are_siblings([7, 4], root))

'''
    1
 2     3
4     5  6
           7

'''
