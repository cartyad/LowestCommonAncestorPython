import unittest
import Node

class Node_test(unittest.TestCase):
    
    def testFirst(self):
        print("This is a test:")
        result =True
        self.assertEquals(result,True,"Oh no")
        '''
        root = Node.tree()
        self.assertEqual(self.Node.findLCA(root, 4, 5),2)
        ''' 
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