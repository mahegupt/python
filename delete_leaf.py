# Python Program to Remove all leaf nodes
# from the binary search tree

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function for inorder traversal in a BST.


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Delete leaf nodes from binary search tree.


def leafDelete(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        del root
        return None

    # Recursively delete in left and right subtrees.
    root.left = leafDelete(root.left)
    root.right = leafDelete(root.right)

    return root


if __name__ == "__main__":

    # Create a hard coded BST.
    #        20
    #       /  \
    #      8   22
    #     / \
    #   4   12
    #       /  \
    #     10   14
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    print(f"Original Tree is ")
    inorder(root)

    leafDelete(root)
    print(f"\nAfter deleteing Leaf nodes, Tree is")
    inorder(root)
