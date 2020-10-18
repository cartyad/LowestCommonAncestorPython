import unittest
import Node

class Node_test(unittest.TestCase):
    
    def testRoot(self):
        root = Node.tree()
        self.assertEquals(root.key,1)
        
    def testRegularNodes(self):
        root = Node.tree()
        
        testNode1 =Node.findLCA(root, 4, 5)
        self.assertEquals(testNode1.key, 2)    
        
        testNode2 =Node.findLCA(root, 2, 5)
        self.assertEquals(testNode2.key, 2)
        
    def testIdenticalNodeInput(self):
        root = Node.tree()
        testNode =Node.findLCA(root, 4, 4)
        self.assertEquals(testNode.key, 4)    
        
        testNode1 =Node.findLCA(root, 5, 5)
        self.assertEquals(testNode1.key, 5)  
        
    def testNegativeNodeValue(self):
        root = Node.tree()
        testNode1 =Node.findLCA(root, -1, 5)
        self.assertEquals(testNode1, None) 
        
        testNode2 =Node.findLCA(root, 1, -5)
        self.assertEquals(testNode2, None) 
        
        testNode3 =Node.findLCA(root, -1, -5)
        self.assertEquals(testNode3, None) 
    
    def testNodeLargerThanBiggestNode(self):
        root = Node.tree()
        testNode1 =Node.findLCA(root, 20, 5)
        self.assertEquals(testNode1, None)  
        
        testNode1 =Node.findLCA(root, 1, 50)
        self.assertEquals(testNode1, None)    
        
        testNode1 =Node.findLCA(root, 100, 50)
        self.assertEquals(testNode1, None) 
        
        