# print a Binary Search Tree (BST) level by level (also known as level-order traversal or Breadth-First Search)

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_bst_levels(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(' '.join(str(val) for val in level_nodes))

# Example usage:
# Construct the BST:
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7


root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(6, TreeNode(5), TreeNode(7))

print_bst_levels(root)
