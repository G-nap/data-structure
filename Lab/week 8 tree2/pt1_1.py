class Node:
  def __init__(self, data , left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.data)

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
        if node.left is None:
          node.left = node.data
          return self.root
        node = node.left
      else:
        if node.right is None:
          node.right = node.data
          return self.root
        node = node.right
        