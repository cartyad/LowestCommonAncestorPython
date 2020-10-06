import math
"""
def findPath(root, path, k):
    if root is None:
        return False
    if root.key ==k:
        return True
    if((root.left!= None and findPath(root.left, path, k)) or (root.right!=None and findPath(root.right, path, k))):
        return True
        path.pop()
        return False

def findLCA(root, n1, n2):
    path1 =[]
    path2 =[]
    if(not findPath(root,path1,n1) or not findPath(root,path2,n2)):
        return -1
    i=0
    while(i< len(path1) and i<len(path2)):
        if path1[i] != path2[i]:
            break
        i+=1
    return path1[i-1]

root = Node(1)
root.left = Node(2)
root.right = Node(3)   
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("LCA(4, 5) = ", (findLCA(root, 4, 5))) 
print("LCA(4, 6) = ", (findLCA(root, 4, 6)))
print("LCA(3, 4) = ", (findLCA(root,3,4))) 
print("LCA(2, 4) = ", (findLCA(root,2, 4))) 
"""

class Node: 
      
    # Constructor to create a new tree node 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
      
# This function returns pointer to LCA of two given 
# values n1 and n2 
# This function assumes that n1 and n2 are present in 
# Binary Tree 
def findLCA(root, n1, n2): 
      
    # Base Case 
    if root is None: 
        return None
  
    # If either n1 or n2 matches with root's key, report 
    #  the presence by returning root (Note that if a key is 
    #  ancestor of other, then the ancestor key becomes LCA 
    if root.key == n1 or root.key == n2: 
        return root  
  
    # Look for keys in left and right subtrees 
    left_lca = findLCA(root.left, n1, n2)  
    right_lca = findLCA(root.right, n1, n2) 
  
    # If both of the above calls return Non-NULL, then one key 
    # is present in once subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca: 
        return root  
  
    # Otherwise check if left subtree or right subtree is LCA 
    return left_lca if left_lca is not None else right_lca 
  
  
# Driver program to test above function 
  
# Let us create a binary tree given in the above example 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
print( "LCA(4,5) = ", findLCA(root, 4, 5).key) 
print("LCA(4,6) = ", findLCA(root, 4, 6).key) 
print("LCA(3,4) = ", findLCA(root, 3, 4).key) 
print("LCA(2,4) = ", findLCA(root, 2, 4).key) 







         
