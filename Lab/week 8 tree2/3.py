"""
ต้นไม้หยาบเป็นต้นไม้แบบ Complete Binary Tree มีทั้งสิ้น N โหนด การเรียกชื่อโหนดจะเรียกเป็นโหนดที่ 
1,2,3,... ไปเรื่อยๆจนถึงโหนดที่ N เริ่มต้นจะเติมค่าตั้งแต่โหนดที่ [N / 2] + 1 ไปจนถึงโหนดที่ N 
ต่อมาจะมีการขีดฆ่าต้นไม้หยาบ จากโหนดลูกสองโหนดใดๆที่อยู่ติดกัน โดยใช้หลักการว่าโหนดพ่อจะเอาค่าของโหนด
ลูกที่มีค่าน้อยที่สุดขึ้นมา แล้วลบค่าของโหนดลูกทั้งสองด้วยค่านั้น ให้นักศึกษาเขียนโปรแกรมเพื่อหาผลรวมโหนด
ภายหลังการขีดฆ่าต้นไม้หยาบ

โดย input จะแบ่เป็น 2 ฝั่งด้วย /
1. ด้านซ้ายจะเป็นจำนวนโหนด (N) โดยรับประกันว่ามีจำนวนโหนดอย่างต่ำที่สุดคือ 3
2. value จำนวน [N / 2] + 1 ค่า เป็นค่าตั้งแต่โหนดที่ [N / 2] + 1 จนถึง N และถ้าหากจำนวน value
 ไม่เท่ากับ [N / 2] + 1 จะแสดงผลลัพธ์เป็น "Incorrect Input"

หมายเหตุ ต้นไม้ในข้อนี้ไม่จำเป็นต้องเป็น Perfect Binary Tree แต่จำเป็นต้องมีจำนวนโหนดเป็นเลขคี่


Enter Input : 7/1 2 3 4
5


Enter Input : 7/1 2 3 4 5
Incorrect Input


Enter Input : 9/5 5 5 5 5
5

"""

import math
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.index = None
        self.level = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.count = 1
        self.totalLevel = 0

    def setCount(self,count):
        if count>5:
            for i in range(count//2):
                self.createBlank('blank',i+1)
        else:
            self.root = Node('blank')
            self.root.level = 1
            self.root.index = 1
            self.count +=1
            self.root.left = Node('blank')
            self.root.left.level = self.root.level+1
            self.root.left.index = self.count 
            self.root.right = Node('blank')
            self.count +=1
            self.root.right.level = self.root.level+1
            self.root.right.index = self.count 
            if count == 5:
                nodeLeft = self.root.left
                nodeLeft.left = Node('blank')
                self.count +=1
                nodeLeft.left.index = self.count 
                nodeLeft.left.level = 2
                nodeLeft.right = Node('blank')
                self.count +=1
                nodeLeft.right.index = self.count 
                nodeLeft.right.level = 2

    def createBlank(self, data,index):
        if index == 1: 
            self.root = Node('blank')
            self.root.index = 1
            self.root.level = 0
        else: 
            Q = [] 
            Q.append(self.root)     
            while len(Q) != 0:
                now = Q.pop(0)
                
                if now.left is None:
                    now.left = Node(data)
                    self.count +=1
                    now.left.parent = now
                    now.left.index = self.count
                    now.left.level = now.level+1
                else: Q.append(now.left)
                if now.right is None:
                    now.right = Node(data)
                    self.count +=1
                    now.right.parent = now
                    now.right.index = self.count
                    now.right.level = now.level+1
                else: Q.append(now.right)

    def insertAt(self,data,index):
        Q = []
        Q.append(self.root)
        while len(Q) != 0:
            now = Q.pop(0)
            if now.left is not None:
                if now.left.index == index: 
                    currentLevel = now.left.level
                    now.left = Node(data)
                    now.left.index = index
                    now.left.parent = now
                    now.left.level = currentLevel
                    break
                else: 
                    Q.append(now.left)
            if now.right is not None:
                if now.right.index == index: 
                    currentLevel = now.right.level
                    now.right = Node(data)
                    now.right.index = index
                    now.right.parent = now
                    now.right.level = currentLevel
                    break
                else: 
                    Q.append(now.right)
        
    def setLevel(self,level):
        minData = 0
        if self.count<6:
            if self.count == 5 and level == 0:
                if self.root.left.left.data < self.root.left.right.data: minData = self.root.left.left.data
                else: minData = self.root.left.right.data 
                self.root.left.data = minData
                self.root.left.left.data -= minData
                self.root.left.right.data -= minData
                if self.root.left.data < self.root.right.data: minData = self.root.left.data
                else: minData = self.root.right.data
                self.root.data = minData
                self.root.left.data -= minData
                self.root.right.data -= minData
            elif self.count == 3 and level == 0:
                if self.root.left.data < self.root.right.data: minData = self.root.left.data
                else: minData = self.root.right.data
                self.root.data = minData
                self.root.left.data -= minData
                self.root.right.data -= minData

        else:
            Q = []
            Q.append(self.root)
            minData = 0
            # 9/1 3 7 2 6
            while len(Q) != 0:
                now = Q.pop(0)
                if now.left is not None or now.right is not None:
                    if level == now.level +1:
                        if now.left.data < now.right.data: minData = now.left.data
                        else: minData = now.right.data
                if now.left is not None:
                    if now.left.level == level:
                        index = now.left.index
                        now.data = minData
                        left = now.left.left
                        right = now.left.right
                        now.left = Node(now.left.data-minData)
                        now.left.index = index
                        now.left.level = level
                        now.left.parent = now
                        now.left.left = left
                        now.left.right = right 
                    else: 
                        Q.append(now.left)
                if now.right is not None:
                    if now.right.level == level:
                        index = now.right.index
                        now.data = minData
                        left = now.right.left
                        right = now.right.right
                        now.right = Node(now.right.data-minData)
                        now.right.left = left
                        now.right.right = right 
                        now.right.index = index
                        now.right.level = level
                        now.right.parent = now
                    else: 
                        Q.append(now.right)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def countNode(self,node):
        Q = [] 
        count = node.data
        Q.append(self.root)     
        while len(Q) != 0:
            now = Q.pop(0) 
            if now.left is not None: 
                count+= now.left.data
                Q.append(now.left)
            if now.right is not None: 
                count+=now.right.data
                Q.append(now.right)
        return count

            
    def markedTree(self):
        count = 0
        return count

T = BST()
inp = input('Enter Input : ').split('/')
inp[1] = [int(i) for i in inp[1].split()]
if int(inp[0])<3 or int(inp[0])%2 == 0 or len(inp[1])!=(int(inp[0])//2+1): 
    print('Incorrect Input')
else: 
    T.setCount(int(inp[0]))

    for i in range(int(inp[0])-len(inp[1])+1):
        T.insertAt(inp[1][i],int(inp[0])-len(inp[1])+i+1) 

    for i in range(int(inp[0])-len(inp[1])):
        T.setLevel(int(inp[0])-len(inp[1])-1-i)

    # T.printTree(T.root)
    print(T.countNode(T.root))