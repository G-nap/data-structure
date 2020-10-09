class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):  #สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
        self.head = None
        self._size = 0

    def __str__(self):   #คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
        if self.isEmpty():
            return 'Empty'
        cur, s = self.head, str(self.head.value) + ' '
        while cur.next != None:
            s += str(cur.next.value) + ' '
            cur = cur.next
        return s

    def isEmpty(self):  #เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
        return self.head == None

    def append(self, item):   #add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
        NewNode  = Node(item)
        if self.head is None:
            self.head = NewNode 
        else:
            laste  = self.head
            while laste.next != None:
                laste  = laste.next
            laste.next = NewNode 
        self._size += 1

    def addHead(self, item):    #add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
        self._size += 1
        if self.isEmpty():
            self.head = Node(item)
            return
        node = self.head
        self.head = Node(item)
        self.head.next = node

    def search(self, item):  #ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
        NewNode = self.head
        if self.isEmpty():
            return 'Not Found'
        while NewNode is not None:
            if NewNode.value == item:
                return 'Found'
            if NewNode == item:
                return NewNode
            NewNode = NewNode.next
        return 'Not Found'

    def index(self, item):   #ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน 
        index = 0              #คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
        node = self.head
        if self.isEmpty():
            return -1
        
        if self.size() == 1:       
            if node.value == item:
                return index

        while node.next != None :
            if node.value == item:
                return index
            node = node.next
            index += 1
        if node.value == item:
            return index
        return -1


    def size(self):         #คืนค่าเป็นขนาดของ Linked List
        return self._size

    def pop(self,pos):      # นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
        index = 0
        if pos >= self.size() or pos < 0:
            return 'Out of Range'
        if pos == 0  and self.size() == 1:
            self.head = self.tail = None
        elif pos == 0:
            self.head.next.previous = None
            self.head = self.head.next
        else:
            node = self.head
            while index != pos - 1:
                index += 1
            node.next = node.next.next
        self._size -= 1
        return 'Success'

inp = input('Enter Input : ').split(',')
l = []
L = LinkedList()
for i in range(len(inp)):
    l.append(inp[i].split())
    if l[i][0] == 'AP':
        L.append(l[i][1])
    elif l[i][0] == 'AH':
        L.addHead(l[i][1])
    elif l[i][0] == 'SE':
        print(f'{L.search(l[i][1])} {l[i][1]} in {L}')
    elif l[i][0] == 'ID': 
        print(f'Index ({l[i][1]}) = {L.index(l[i][1])} : {L}')
    elif l[i][0] == 'SI': 
        print(f'Linked List size = {L.size()} : {L}')
    elif l[i][0] == 'PO': 
        txt = f'{L}'
        p = L.pop(int(l[i][1]))
        print(f'{p} | {txt}-> {L}' if p == 'Success' else f'{p} | {L}') 
print('Linked List :', L)