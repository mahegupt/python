# To clone a Binary Search Tree (BST) means to create an exact copy of the given tree structure and its node values, but with all new node instances.

# High-level Approach
# Traverse the original BST (using any traversal: pre-order is common).
# For each node, create a new node with the same value.
# Recursively clone the left and right subtrees.
# Return the new root node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def cloneBST(root):
    if root is None:
        return None
    new_root = TreeNode(root.val)
    new_root.left = cloneBST(root.left)
    new_root.right = cloneBST(root.right)
    return new_root


root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(7, TreeNode(6), TreeNode(8))

clone = cloneBST(root)
