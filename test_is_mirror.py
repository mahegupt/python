import unittest
from is_mirror import Node, is_mirror


class TestIsMirror(unittest.TestCase):
    def test_identical_trees(self):
        a = Node(1)
        a.left = Node(2)
        a.right = Node(3)
        b = Node(1)
        b.left = Node(2)
        b.right = Node(3)
        self.assertFalse(is_mirror(a, b))

    def test_mirror_trees(self):
        a = Node(1)
        a.left = Node(2)
        a.right = Node(3)
        b = Node(1)
        b.left = Node(3)
        b.right = Node(2)
        self.assertTrue(is_mirror(a, b))

    def test_single_node(self):
        a = Node(1)
        b = Node(1)
        self.assertTrue(is_mirror(a, b))

    def test_none_nodes(self):
        self.assertTrue(is_mirror(None, None))
        a = Node(1)
        self.assertFalse(is_mirror(a, None))
        self.assertFalse(is_mirror(None, a))

    def test_complex_mirror(self):
        a = Node(1)
        a.left = Node(2)
        a.right = Node(3)
        a.left.left = Node(4)
        a.right.right = Node(5)
        b = Node(1)
        b.left = Node(3)
        b.right = Node(2)
        b.left.left = Node(5)
        b.right.right = Node(4)
        self.assertTrue(is_mirror(a, b))


if __name__ == "__main__":
    unittest.main()
