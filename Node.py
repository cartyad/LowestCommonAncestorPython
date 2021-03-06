
class Node: 
      
    
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
      
def findLCAUtil(root, n1, n2, v): 

    if root is None: 
        return None
  
    if root.key == n1 : 
        v[0] = True
        return root 
  
    if root.key == n2: 
        v[1] = True
        return root 

    left_lca = findLCAUtil(root.left, n1, n2, v) 
    right_lca = findLCAUtil(root.right, n1, n2, v) 

    if left_lca and right_lca: 
        return root  

    return left_lca if left_lca is not None else right_lca 

def find(root, k): 
      
    if root is None: 
        return False

    if (root.key == k or find(root.left, k) or
        find(root.right, k)): 
        return True

    return False        

def findLCA(root, n1, n2): 
      
    v = [False, False] 

    lca = findLCAUtil(root, n1, n2, v) 
 
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and 
        find(lca, n1)): 
        return lca 

    return None

def tree():
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7)
    return root

def nullTree():
    root=None
    return root


'''  
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

lca = findLCA(root, -1, 5) 
if lca is not None: 
    print("LCA(-1,5) = ", lca.key) 
else: 
    print("LCA(-1,5) Keys are not present")   

lca = findLCA(root, 40, 10) 
if lca is not None: 
    print("LCA(40,10) = ", lca.key) 
else: 
    print("LCA(40,10) Keys are not present")   

lca = findLCA(root, 2, 5) 
if lca is not None: 
    print("LCA(2, 5) = ", lca.key) 
else : 
    print("LCA(2, 5) Keys are not present")   

lca = findLCA(root, 4, 4) 
if lca is not None: 
    print("LCA(4, 4) = ", lca.key) 
else : 
    print("LCA(4, 4) Keys are not present")     
'''