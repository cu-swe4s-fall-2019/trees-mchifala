import unittest
import random
import os
import numpy as np
import sys
from binary_tree import insert
from binary_tree import insert_helper
from binary_tree import search
from binary_tree import Node
from insert_key_values_pairs import get_data
from a import avl


class TestTree(unittest.TestCase):

    def inorder(self, root, ordered_keys):
        """
        This helper function returns a list of keys from doing
        an inorder traversal of BST. The keys should be ordered.

        """
        if root:
            self.inorder(root.left, ordered_keys)
            ordered_keys.append(root.key)
            self.inorder(root.right, ordered_keys)

        return ordered_keys

    def make_random_tree(self, n):
        """
        This helper function makes a random BST and returns its root and keys

        """
        self.root = Node(random.randint(0, 100), random.randint(0, 100))
        self.keys = [self.root.key]
        for i in range(n):
            key, value = random.randint(0, 100), random.randint(0, 100)
            if key not in self.keys:
                self.keys.append(key)
                insert(self.root, key, value)
        return self.root, self.keys

    def make_avl_tree(self, n):
        """
        This helper function makes a random AVL and returns its root and keys

        """
        self.keys = []
        self.avl_tree = avl.AVL()
        for i in range(n):
            key = random.randint(0, 100)
            if key not in self.keys:
                self.keys.append(key)
                self.avl_tree.insert(key)
        return self.avl_tree, self.keys

    def test_get_data(self):
        """
        This function tests that random data is being imported correctly

        """
        self.key_values = get_data("test.txt", 10)
        self.kv = [(str(x), str(x)) for x in range(1, 11)]
        self.assertEqual(self.key_values, self.kv)

    def test_get_data_empty(self):
        """
        This function tests that random data is being imported correctly

        """
        self.key_values = get_data("test.txt", 0)
        self.assertEqual(self.key_values, [])

    def test_avl_insert_many(self):
        """
        This test makes sure that random keys are properly inserted
        into AVL tree and maintain the BST property.

        """
        self.n = 10
        self.avl_tree, self.keys = self.make_avl_tree(self.n)
        self.assertEqual(self.inorder(self.avl_tree.root, []),
                         sorted(self.keys))

    def test_avl_insert_one(self):
        """
        This test makes sure that the root key is properly inserted into AVL.

        """
        self.n = 1
        self.avl_tree, self.keys = self.make_avl_tree(self.n)
        self.assertEqual(self.inorder(self.avl_tree.root, []),
                         sorted(self.keys))

    def test_avl_search(self):
        """
        This functions makes sure that the search function is
        correctly searching the AVL for a given key and returning its value

        """
        self.n = 10
        self.avl, self.keys = self.make_avl_tree(self.n)
        insert(self.avl.root, 50.5, "Successful search")
        self.assertEqual(search(self.avl.root, 50.5), "Successful search")

    def test_tree_insert_many(self):
        """
        This test makes sure that random keys are properly inserted
        into tree and maintain the BST property.

        """
        self.n = 10
        self.root, self.keys = self.make_random_tree(self.n)
        self.assertEqual(self.inorder(self.root, []), sorted(self.keys))

    def test_tree_insert_root(self):
        """
        This test makes sure that root is properly inserted.

        """
        self.root = Node(random.randint(0, 100), random.randint(0, 100))
        self.keys = [self.root.key]
        self.assertEqual(self.inorder(self.root, []), sorted(self.keys))

    def test_tree_search(self):
        """
        This functions makes sure that the search function is
        correctly searching the BST for a given key and returning its value

        """
        self.n = 10
        self.root, self.keys = self.make_random_tree(self.n)
        insert(self.root, 50.5, "Successful search")
        self.assertEqual(search(self.root, 50.5), "Successful search")


if __name__ == '__main__':
    unittest.main()
