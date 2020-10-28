"""
บริษัทแห่งหนึ่งมีรถตู้ K คันที่ลูกค้าสามารถเช่าไปใช้งานได้ โดยรถตู้แต่ละคันมีรหัสประจำตัวรถเป็นหมายเลข
จำนวนเต็มบวกตั้งแต่ 1 จนถึง K ข้อกำหนดในการเลือกรถตู้ให้ลูกค้ามีอยู่ว่า ลูกค้าจะต้องทำการจองรถตู้ก่อน 
โดยคำสั่งจองจะต้องระบุจำนวนวันที่จะใช้ 
จากนั้นผู้จองจะได้รถตู้ที่ว่างให้ใช้เร็วที่สุดเท่าที่จะหาได้จากรถตู้ทั้งหมด

ในกรณีที่มีรถตู้ว่างให้ใช้เร็วที่สุดมากกว่า 1 คัน คันที่มีรหัสประจำรถน้อยกว่าจะถูกเลือกก่อน 
เช่นถ้าหากมีรถตู้ที่ว่างให้ใช้เร็วที่สุด 3 คัน  ซึ่งมีรหัสประจำรถเป็น 5 , 7 และ 20 รถตู้ที่มีหมายเลข 5 
จะถูกเลือกก่อน นอกจากนี้การจองจะให้ความสำคัญกับคำสั่งจองที่มาก่อนเสมอ สำหรับการจองแต่ละครั้ง 
ผู้จองจะได้รับคำตอบกลับมาว่าได้ใช้รถตู้หมายเลขใด  โดยในตอนแรกรถตู้ทุกคันจะว่างและพร้อมใช้งานทั้งหมด

อธิบาย Input โดย Input จะแบ่งเป็น 2 ฝั่งด้วย /
-  ฝั่งซ้ายเป็น K ซึ่งหมายถึงเลขประจำตัวรถ โดยเริ่มตั้งแต่ 1 ถึง K
-  ฝั่งขวาเป็น List จำนวนวันที่จองรถตู้ของลูกค้าที่สั่งจองเข้ามา

Enter Input : 3/3 1 2 2 2 1
Customer 1 Booking Van 1 | 3 day(s)
Customer 2 Booking Van 2 | 1 day(s)
Customer 3 Booking Van 3 | 2 day(s)
Customer 4 Booking Van 2 | 2 day(s)
Customer 5 Booking Van 3 | 2 day(s)
Customer 6 Booking Van 1 | 1 day(s)


Enter Input : 5/1 1 1 1 1 1 1 1 1
Customer 1 Booking Van 1 | 1 day(s)
Customer 2 Booking Van 2 | 1 day(s)
Customer 3 Booking Van 3 | 1 day(s)
Customer 4 Booking Van 4 | 1 day(s)
Customer 5 Booking Van 5 | 1 day(s)
Customer 6 Booking Van 1 | 1 day(s)
Customer 7 Booking Van 2 | 1 day(s)
Customer 8 Booking Van 3 | 1 day(s)
Customer 9 Booking Van 4 | 1 day(s)


"""

class Node:
    def __init__(self, name, pos, data):
        self.name = name
        self.pos = pos
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.name)

class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def enqueue(self, data):
        self.item.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, name, pos, data = 0):
        if not self.root:
            self.root = Node(name, pos, data)
            return
        if pos == node.pos * 2 + 1:
            node.left = Node(name, pos, data)
            return node
        if pos == node.pos * 2 + 2:
            node.right = Node(name, pos, data)
            return node
        if node.left:
            node.left = self.insert(node.left, name, pos, data)
        if node.right:
            node.right = self.insert(node.right, name, pos, data)
        return node

    def book(self, data):
        L = []
        self.root.data += data
        R = self.root 
        Q = Queue()
        Q.enqueue(self.root.left)
        Q.enqueue(self.root.right)

        while not Q.is_empty():
            node = Q.dequeue()
            if node.left is not None:
                Q.enqueue(node.left)
            if node.right is not None:
                Q.enqueue(node.right)

            if R and R.data < node.data:
                R.left = R.right = None
                L.append(R)
                R = None

            if R and R.data == node.data:
                if R.name < node.name:
                    R.left = R.right = None
                    L.append(R)
                    R = None

            node.left = node.right = None
            L.append(node)
            if R and R.data == node.data:
                if R.name > node.name:
                    R.left = R.right
                    L.append(R)
                    R = None
        if R:
            L.append(R)
        self.root = None
        return L

def printTree(data, index, size, level):
    if  index < size:
        printTree(data, 2 * index + 2, size, level + 1)
        print('        ' * level, data[index])
        printTree(data, 2 * index + 1, size, level + 1)

if __name__ == "__main__":
    Inp = input('Enter Input : ').split('/')

    data = []
    van = {}

    for name in range(int(Inp[0])):
        van[name + 1] = van.get(name + 1, 0)
        data.append(int(name) + 1)

    for customer, x in enumerate(Inp[1].split()):
        #printTree(data, 0, len(data), 0)
        print(f'Customer {customer + 1} Booking Van {data[0]} | {x} day(s)')
        #print('--------------------------------------------------')
        p = data.pop(0)
        van[p] = van.get(p, 0) + int(x)
        for index, x in enumerate(data):
            if  van[p] < van[x] or (van[p] == van[x] and p < x):
                data.insert(index, p)
                p = None
                break
        if p:
            data.append(p)


