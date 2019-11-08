import unittest
import random
import os
import numpy as np
import sys
from binary_tree import insert
from binary_tree import insert_helper
from binary_tree import search
from binary_tree import Node

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
    
    def make_random_tree(self):
        """
        This helper function makes a random BST and returns its root and keys
        
        """
        self.root = Node(random.randint(0,100), random.randint(0,100))
        self.keys = [self.root.key]
        for i in range(10):
            key, value = random.randint(0,100), random.randint(0,100)
            if key not in self.keys:
                self.keys.append(key)
                insert(self.root, key, value)
        return self.root, self.keys
    
    def test_tree_insert_many(self):
        """
        This test makes sure that random keys are properly inserted 
        into tree and maintain the BST property.
        
        """
        self.root, self.keys = self.make_random_tree()
        self.assertEqual(self.inorder(self.root, []), sorted(self.keys))
        
    def test_tree_insert_root(self):
        """
        This test makes sure that root is properly inserted.
        
        """
        self.root = Node(random.randint(0,100), random.randint(0,100))
        self.keys = [self.root.key]
        self.assertEqual(self.inorder(self.root, []), sorted(self.keys))
    
    def test_search(self):
        """
        This functions makes sure that the search function is 
        correctly searching the BST for a given key and returning its value
        
        """
        self.root, self.keys = self.make_random_tree() 
        insert(self.root, 50.5, "Successful search")
        self.assertEqual(search(self.root, 50.5), "Successful search")
        
if __name__ == '__main__':
    unittest.main()