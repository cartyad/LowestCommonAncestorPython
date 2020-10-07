import math
class Node: 
      
    
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
      
def findLCAKey(root,n1,n2):
    if(findLCA(root, n1, n2)==None):
        return -1

    if findLCA(root, n1,n2) != None:
        LCANode=findLCA(root, n1,n2)
        return LCANode.key

def findLCA(root, n1, n2): 
       
    if root is None: 
        return None

    if n1<0 or n2<0:
        return None
  
    if root.key == n1 or root.key == n2: 
        return root  
    """
    if root.left==None and root.right==None:
        return None

    if root.left==None and root.right!=None:
        right_lca = findLCA(root.right, n1, n2) 

    if root.right==None and root.left!=None:
        left_lca = findLCA(root.left, n1, n2)     
    """

    left_lca = findLCA(root.left, n1, n2)  
    right_lca = findLCA(root.right, n1, n2) 
    
    if left_lca and right_lca: 
        return root  
   
    return left_lca if left_lca is not None else right_lca
    
    
  
root = Node(5) 
root.left = Node(7) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(3) 
root.right.left = Node(2) 
root.right.right = Node(4) 
print("An error or non-existent LCA will appear as")
print( "LCA(1,3) = ", findLCAKey(root, 1, 3)) 
print("LCA(1,2) = ", findLCAKey(root, 1, 2)) 
print("LCA(1,6) = ", findLCAKey(root, 1, 6)) 
print("LCA(1,7) = ", findLCAKey(root, 1, 7)) 
