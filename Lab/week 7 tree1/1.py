"""
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)

Enter Input : 10 4 20 1 5
      20
 10
           5
      4
           1

Enter Input : 4 10 3 6 13 9
           13
      10
                9
           6
 4
      3

Enter Input : 1 2 3 4 5 6 7 8 0 -1 -2
                                    8
                               7
                          6
                     5
                4
           3
      2
 1
      0
           -1
                -2


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
        print('      ' * level, node)
        self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
  root = T.insert(i)
T.printTree(root)

