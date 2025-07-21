# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_zigzag_levels(root):
    result = []
    count = 0
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

        if count % 2:
            nodes_per_level.reverse()
        result.append(nodes_per_level)
        count += 1
    return result


# Example unbalanced tree:
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(13)
root.left.right = TreeNode(23)

print(print_zigzag_levels(root))
