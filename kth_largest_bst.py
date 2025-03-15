class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Example BST:
#        5
#       / \
#      3   7
#     / \  / \
#    2  4 6  8
class Solution:
    def __init__(self):
        self.ans = None

    def dfs(self, root, k):
        if not root:
            return
        self.dfs(root.right, k)
        k[0] -= 1
        if k[0] == 0:
            self.ans = root.val
            return
        self.dfs(root.left, k)

    def kthLargest(self, root, k):
        kref = [k]
        self.dfs(root, kref)
        return self.ans

'''
Start from root, keep moving to largest side(right) and store all elements on stack.
Once you reached end, you have largest element on top of stack. keep poping, adding the left child to stack as it is bigger than their parent.
'''
class iSolution:
    def kthLargest(self, root, k):
        stack = []
        while(root or stack):
            while(root):
                stack.append(root)
                root = root.right

            root = stack.pop()
            k -= 1
            if k==0:
                return root.val
            root = root.left



# Example BST:
#        5
#       / \
#      3   7
#     / \  / \
#    2  4 6  8

root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(7, TreeNode(6), TreeNode(8))

sol = Solution()
print(sol.kthLargest(root, 3))  # Output: 6 (3rd largest)
isol = iSolution()
print(isol.kthLargest(root, 3))  # Output: 6 (3rd largest)