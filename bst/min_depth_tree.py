from collections import deque

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    if not root:
        return 0
    # Store all nodes at a level with depth starting 1.
    queue = deque([(root, 1)])

    while queue:
        # While there are nodes, pop them up with their depth, append next level nodes with corrected depth.
        # If it is leaf node, return the current's node depth.
        node, depth = queue.popleft()

        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth+1))
        if node.right:
            queue.append((node.right, depth+1))
    return 0


# Example unbalanced tree:
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(13)
root.left.right = TreeNode(23)

print(min_depth(root))
