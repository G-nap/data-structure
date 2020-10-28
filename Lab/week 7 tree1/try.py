# Python program to print the parent of given node in a binary tree
  
# Creating the Node class 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, value): 
        self.value= value  
        self.left = None
        self.right = None
  
# If target is present in tree, then prints the parent node
def printParent(root, target): 
      
    
    if root == None: 
        return False 
      
    if root.value == target: 
        return True 
  
    # If target is present in tree, then prints the parent node
    if (printParent(root.left, target) or 
        printParent(root.right, target)): 
        print (root.value)
  
# Formation of the binary tree                                                               
root = Node(1)                                                    
root.left = Node(3)
root.right = Node(5)                                               
root.right.left = Node(4)
root.right.right = Node(6)                                          
root.right.right.left = Node(7)      
  
printParent(root, 7)