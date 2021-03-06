from binarytree import tree, bst, heap, build

# Generate a random binary tree and return its root node.
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node.
my_bst = bst(height=3, is_perfect=True)

# Generate a random max heap and return its root node.
my_heap = heap(height=3, is_max=True, is_perfect=False)

# Pretty-print the trees in stdout.
print(my_tree)
print(my_bst)
print(my_heap)

a_tree = build([0,1,2,3,4,5])
a_tree.pprint()