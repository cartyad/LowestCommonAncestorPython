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
      
    v = [False, False] 

    lca = findLCAUtil(root, n1, n2, v) 
 
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and 
        find(lca, n1)): 
        return lca 

    return None
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)
lca = findLCA(root, 4, 5) 
if lca is not None: 
    print("LCA(4, 5) = ", lca.key) 
else : 
    print("LCA(4, 5) Keys are not present")
  
lca = findLCA(root, 4, 10) 
if lca is not None: 
    print("LCA(4,10) = ", lca.key) 
else: 
    print("LCA(4,10) Keys are not present")

lca = findLCA(root, -1, 10) 
if lca is not None: 
    print("LCA(-1,10) = ", lca.key) 
else: 
    print("LCA(-1,10) Keys are not present")   

lca = findLCA(root, 40, 10) 
if lca is not None: 
    print("LCA(40,10) = ", lca.key) 
else: 
    print("LCA(40,10) Keys are not present")   
