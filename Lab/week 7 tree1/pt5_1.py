class Node:
  def __init__(self, data, left = None, right = None):
    self.data = data
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.data)
class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.isEmpty():
      return self.items.pop()

  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)

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
          node.left = node.data
          return self.root
        node = node.left
      else:
        if node.right == None:
          node.right = node.data
          return self.root
        node = node.right

  def preOrder(self, node):
    if node == None:
      return ''
    s = str(node.data) + self.preOrder(node.left) + self.preOrder(node.right)
    return s


  def in_order(self, node):
    if node == None:
      return ''
    s = self.in_order(node.left)+ str(node.data)+ self.in_order(node.right)
    if node.left is not None and node.right is not None:
      s = '(' + s + ')'
    return s


  def printTree(self, node, level = 0):
    if node:
      self.printTree(node.right, level+1)
      print('     ' * level, node)
      self.printTree(node.left, level+1)

inp = list(input('Enter Postfix : '))
t = BST()
s = Stack()

for char in inp:
  if char in '+-*/':
    op1 = s.pop()
    op2 = s.pop()
    s.push(Node(char, op1, op2))
  else:
    s.push(Node(char))
  
print('Tree : ')
root = s.pop()
t.printTree(root)
print("--------------------------------------------------")
print('Prefix : ',t.preOrder(root))
print('Infix : ',t.in_order(root))