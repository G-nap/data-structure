"""
Enter Input : 10 4 20 1 5
Preorder : 10 4 1 5 20 
Inorder : 1 4 5 10 20 
Postorder : 1 5 4 20 10 
Breadth : 10 4 20 1 5 


Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100
Preorder : 0 -50 -75 -100 -62 -25 -38 -13 50 25 13 28 75 62 100 
Inorder : -100 -75 -62 -50 -38 -25 -13 0 13 25 28 50 62 75 100 
Postorder : -100 -62 -75 -38 -13 -25 -50 13 28 25 62 100 75 50 0 
Breadth : 0 -50 50 -75 -25 25 75 -100 -62 -38 -13 13 28 62 100 

"""

class Node:
    def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
    
    def __str__(self):
      return str(self.data)

class Queue:
    def __init__(self):
      self.items = []

    def is_empty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)

    def enqueue(self, data):
      self.items.append(data)

    def dequeue(self):
      if not self.is_empty():
        return self.items.pop(0)

class BST:
    def __init__(self):
      self.root = None

    def insert(self, data):
      if self.root is None:
        self.root = Node(data)
        return self.root
      node = self.root
      while True:
        if data < node.data:
          if node.left == None:
            node.left = Node(data)
            return self.root
          node = node.left
        else:
          if node.right == None:
            node.right = Node(data)
            return self.root
          node = node.right
    
    def pre_order(self, node):
        if node == None:
          return ''
        s = str(node.data) + ' '+ self.pre_order(node.left) + self.pre_order(node.right)
        return s

        # print(node.data, end = ' ')
        # self.pre_oder(node.left)
        # self.pre_oder(node.right)

    def in_order(self, node):
        if node == None:
          return ''

        s = self.in_order(node.left)  + str(node.data) + ' ' + self.in_order(node.right)
        return s

        # self.in_oder(node.left)
        # print(node.data, end = ' ')
        # self.in_oder(node.right)

    def post_order(self, node):
        if node == None:
          return ''
        
        s = self.post_order(node.left)+ self.post_order(node.right) + str(node.data) + ' '
        return s

        # self.post_order(node.left)
        # self.post_order(node.right)
        # print(node.data, end = ' ')

    def BFS(self): 
        q = Queue()
        q.enqueue(self.root)
        s = "Breadth : "
        while not q.is_empty():
            node = q.dequeue()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return s

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
  root = T.insert(i)
    
print('Preorder :', T.pre_order(root))
print('Inorder :', T.in_order(root))
print('Postorder :', T.post_order(root))
print(T.BFS())