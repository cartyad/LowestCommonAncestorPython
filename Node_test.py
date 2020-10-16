import unittest
import Node

class Node_test(unittest.TestCase):

    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7)

    def First_test(self):
        self.assertEqual(Node.findLCA(root, 4, 5),2)
'''    
    def tree():
        root = Node(1) 
        root.left = Node(2) 
        root.right = Node(3) 
        root.left.left = Node(4) 
        root.left.right = Node(5) 
        root.right.left = Node(6) 
        root.right.right = Node(7)
    
    def simpleTest(self):
        tree()
        self.assertEqual(findLCA(root,4,5),2)
'''