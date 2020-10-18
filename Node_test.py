import unittest
'''import Node'''

class Node_test(unittest.TestCase):
    
    def First_test(self):
        print("This is a test:")
        result =True
        self.assertEquals(result,True,"Oh no")
        '''
        root = self.Node.tree()
        self.assertEqual(self.Node.findLCA(root, 4, 5),2)
        '''    