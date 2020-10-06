import math
class Node: 
      
    
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
      
def findLCA(root, n1, n2): 
       
    if root is None: 
        return None

    if n1<0 or n2<0:
        return None
  
    if root.key == n1 or root.key == n2: 
        return root  
  
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
print( "LCA(1,3) = ", findLCA(root, 1, 3).key) 
print("LCA(1,2) = ", findLCA(root, 1, 2).key) 
print("LCA(1,6) = ", findLCA(root, 1, 6).key) 
print("LCA(1,7) = ", findLCA(root, 1, 7).key) 







         
