"""
กฤษฎาได้ค้นพบเม็ดถั่ววิเศษที่เมื่อโยนลงดินแล้วถั่วจะสามารถเติบโตขึ้นและกลายเป็น Binary Search Tree (BST) ได้ โดยงานของนักศึกษาก็คือนักศึกษาจะต้องสร้าง BST 
ตามลำดับของข้อมูลนำเข้าซึ่งเป็นตัวเลขจำนวนเต็มที่ไม่ซ้ำกันเลย โดยในการใส่ค่าในแต่ละครั้งจะกลับมาที่ Root of BST เสมอ  แล้วท่องต้นไม้ไปทางซ้ายด้วยคำสั่ง "L" 
หรือท่องต้นไม้ไปทางขวาด้วยคำสั่ง "R" จนกว่าจะถึงตำแหน่งที่เหมาะสมที่จะใส่ข้อมูลแล้วจึงพิมพ์ "*" เพื่อใส่ข้อมูลลงไปในต้นไม้  
จงเขียนโปรแกรมเพื่อแสดงคำสั่งการท่องต้นไม้ในการใส่ข้อมูลทีละค่าตามลำดับของข้อมูลนำเข้า

1.

Enter Input : 1 2 5 4 3 -2 -1
*
R*
RR*
RRL*
RRLL*
L*
LR*

2.

Enter Input : 48 47 194194 3534 39 20 2014 35289 53
*
L*
R*
RL*
LL*
LLL*
RLL*
RLR*
RLLL*

"""

class Node:
  def __init__(self, data, left = None, right = None):
    self.data = data
    self.left = left
    self.right= right

  def __str__(self):
    return str(self.data)

class BST:
  def __init__(self):
    self.root = None
    
  def insert(self, data):
    if not self.root:
      self.root = Node(data)
    else:
      self.insert_recur(self.root, data)
    print("*")
    return self.root

  def insert_recur(self, node, data):
    if node.data > data:
      print("L", end= '')
      if not node.left:
        node.left = Node(data)
      else:
        self.insert_recur(node.left, data)
    else:
      print("R", end='')
      if not node.right:
        node.right = Node(data)
      else:
        self.insert_recur(node.right, data)

inp = list(map(int, input("Enter Input : ").split()))
bst = BST()
for e in inp:
    root = bst.insert(e)