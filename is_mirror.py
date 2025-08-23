from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_mirror(a, b):
    if a == None and b == None:
        return True
    if a == None or b == None:
        return False
    return (a.val == b.val and is_mirror(a.left, b.right) and is_mirror(a.right, b.left))


def is_mirror_iter(a, b):
    # Queue for node
    queue = deque()
    queue.append((a, b))
    while (queue):
        n1, n2 = queue.popleft()
        # If both have same value.
        if n1 is None and n2 is None:
            continue

        # Return false if there is mismatch
        if n1 is None or n2 is None or n1.val != n2.val:
            return False

        queue.append((n1.left, n2.right))
        queue.append((n1.right, n2.left))

    return True


if __name__ == "__main__":
    a = Node(10)
    a.left = Node(8)
    a.right = Node(12)

    b = Node(10)
    b.left = Node(8)
    b.right = Node(12)

    print(f"Both tree a and b are mirror:{is_mirror(a, b)}")
    print(f"Both tree a and b are mirror:{is_mirror_iter(a, b)}")

    b = Node(10)
    b.left = Node(12)
    b.right = Node(8)

    print(f"Both tree a and b are mirror:{is_mirror(a, b)}")
    print(f"Both tree a and b are mirror:{is_mirror_iter(a, b)}")

    # Tree 1
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.right.right = Node(5)

    # Tree 2
    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)
    root2.left.left = Node(5)
    root2.right.right = Node(4)

    print(is_mirror(root1, root2))  # Output: True
    print(is_mirror_iter(root1, root2))  # Output: True
