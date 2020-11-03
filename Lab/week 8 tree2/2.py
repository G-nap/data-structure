"""
ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert ให้ตรวจสอบว่า balance หรือยัง หากไม่ให้ ปรับ Balance ให้เรียบร้อยแล้วและแสดงผล

** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

#code เป็นเพียงตัวอย่างเท่านั้นสามารถเขียนขึ้นเองโดยไม่ต้องอ้างอิงจาก code นี้ก็ได้


class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    #code here

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")


1.

Enter Input : 1 2 3 4 5 6 7 8
insert : 1
 1
===============
insert : 2
      2
 1
===============
insert : 3
Not Balance, Rebalance!
      3
 2
      1
===============
insert : 4
           4
      3
 2
      1
===============
insert : 5
Not Balance, Rebalance!
           5
      4
           3
 2
      1
===============
insert : 6
Not Balance, Rebalance!
           6
      5
 4
           3
      2
           1
===============
insert : 7
Not Balance, Rebalance!
           7
      6
           5
 4
           3
      2
           1
===============
insert : 8
                8
           7
      6
           5
 4
           3
      2
           1
===============


2.

Enter Input : 50 40 35 30 20 10 5
insert : 50
 50
===============
insert : 40
 50
      40
===============
insert : 35
Not Balance, Rebalance!
      50
 40
      35
===============
insert : 30
      50
 40
      35
           30
===============
insert : 20
Not Balance, Rebalance!
      50
 40
           35
      30
           20
===============
insert : 10
Not Balance, Rebalance!
           50
      40
           35
 30
      20
           10
===============
insert : 5
Not Balance, Rebalance!
           50
      40
           35
 30
           20
      10
           5
===============


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL(object): 

    def __init__(self):
        self.root = None

    def insert(self, node, data): 
      
        if not node:
            node = Node(data)
            return node
        elif data < node.data: 
            node.left = self.insert(node.left, data) 
        else: 
            node.right = self.insert(node.right, data) 
  
        node.height = 1 + max(self.getHeight(node.left), 
                           self.getHeight(node.right)) 
  
        balance = self.getBalance(node) 
  
        # Case 1 - Left Left 
        if balance > 1 and data < node.left.data: 
            print('Not Balance, Rebalance!')
            return self.right_rotate(node) 
  
        # Case 2 - Right Right 
        if balance < -1 and data >= node.right.data: 
            print('Not Balance, Rebalance!')   
            return self.left_rotate(node) 
  
        # Case 3 - Left Right 
        if balance > 1 and data >= node.left.data: 
            print('Not Balance, Rebalance!') 
            node.left = self.left_rotate(node.left) 
            return self.right_rotate(node) 
  
        # Case 4 - Right Left 
        if balance < -1 and data < node.right.data:  
            print('Not Balance, Rebalance!') 
            node.right = self.right_rotate(node.right) 
            return self.left_rotate(node) 
  
        return node 
  
    def left_rotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        y.left = z 
        z.right = T2 
  
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 

        return y 
  
    def right_rotate(self, z): 
  
        y = z.left 
        T3 = y.right 

        y.right = z 
        z.left = T3 
  
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 

        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == '__main__':
    inp = input('Enter Input : ').split()

    myTree = AVL() 

    for data in inp:
        print(f'insert : {data}')
        myTree.root = myTree.insert(myTree.root, int(data))
        myTree.printTree(myTree.root)
        print('===============')

