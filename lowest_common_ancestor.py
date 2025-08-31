# To find the Lowest Common Ancestor (LCA) of two nodes in a binary tree (not necessarily a BST), you can use recursion:

# Algorithm
# If the current node is None, return None.
# If the current node is either of the two nodes, return the current node.
# Recursively search for the nodes in the left and right subtrees.
# If both sides return non-None, the current node is the LCA.
# If only one side is non-None, propagate that upwards.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root  # p in one side, q in other → root is LCA
        return left if left else right


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left       # 5
q = root.left.right.right  # 4
s = Solution()
lca = s.lowestCommonAncestor(root, p, q)
print("LCA:", lca.val)  # Output: 5
