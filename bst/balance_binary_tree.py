# Given a binary tree, determine if it is height-balanced.
# Also print the height or diagnose where imbalance happens

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced_with_debug(root):
    def check(node):
        if not node:
            return 0  # height of empty subtree

        left_height = check(node.left)
        if left_height == -1:
            return -1  # left subtree is unbalanced

        right_height = check(node.right)
        if right_height == -1:
            return -1  # right subtree is unbalanced

        if abs(left_height - right_height) > 1:
            print(f"⚠️  Imbalance detected at node {node.val}: "
                  f"left height = {left_height}, right height = {right_height}")
            return -1
        else:
            height = max(left_height, right_height) + 1
            print(f"✅ Node {node.val} is balanced, height = {height}")
            return height

    result = check(root)
    if result == -1:
        print("\nFinal Verdict: ❌ Tree is NOT balanced")
        return False
    else:
        print("\nFinal Verdict: ✅ Tree IS balanced")
        return True


# Example unbalanced tree:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(3)

is_balanced_with_debug(root)
