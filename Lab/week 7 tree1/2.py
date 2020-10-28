"""
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

จากนั้นหาความสูงของ Binary Search Tree  นั้น

Enter Input : 3 5 2 1 4 6
Height of this tree is : 2

Enter Input : 3 5 2 1 4 6 7
Height of this tree is : 3

Enter Input : 1
Height of this tree is : 0

"""

class Node:
    def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = None 
      self.right = None 
      
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
      self.root = None

    def insert(self, data):
      if self.root is None:
        self.root = Node(data)
      else:
        fp = None
        p = self.root
        while p:
          fp = p
          if data < p.data:
            p = p.left
          else:
            p = p.right

        if data < fp.data:
          fp.left = Node(data)
        else:
          fp.right  = Node(data)
      return self.root

    def printTree(self, node, level = 0):
      if node is not None:
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

    def maxDepth(self, node): 
      if node is None: 
        return 0 
      else: 
        lDepth = self.maxDepth(node.left) 
        rDepth = self.maxDepth(node.right) 
        if (lDepth > rDepth): 
          return lDepth+1
        else: 
          return rDepth+1
   


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
  root = T.insert(i)
#T.printTree(root)

print("Height of this tree is :",T.maxDepth(root)-1)