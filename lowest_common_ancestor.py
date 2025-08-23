# To find the Lowest Common Ancestor (LCA) of two nodes in a binary tree (not necessarily a BST), you can use recursion:

# Algorithm
# If the current node is None, return None.
# If the current node is either of the two nodes, return the current node.
# Recursively search for the nodes in the left and right subtrees.
# If both sides return non-None, the current node is the LCA.
# If only one side is non-None, propagate that upwards.
