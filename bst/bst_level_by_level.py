# Given a binary tree, determine if it is height-balanced.
# Also print the height or diagnose where imbalance happens
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_levels(root):
    result = []
    if not root:
        return result

    queue = deque([root])
    while queue:
        n = len(queue)
        nodes_per_level = []
        for _ in range(n):
            node = queue.popleft()
            nodes_per_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(nodes_per_level)
    return result


# Example unbalanced tree:
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(13)
root.left.right = TreeNode(23)

print(print_levels(root))
