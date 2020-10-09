class Node():
    def __init__(self, item=None):
        self.item = item
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()

    def __str__(self):
        return " ".join(str(e) for e in self.show())

    def append(self, item):
        newNode = Node(item)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        newNode.perv = cur
        cur.next = newNode

    def isEmpty(self):
        return self.head.next == None

    def show(self):
        li = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            li.append(cur.item)
        return li

    def insert(self, index, item):
        if index > self.lenght() or index < 0:
            return None
        elif index == 0:
            self.appendHead(item)
            return self.show()
        elif index == self.lenght():
            self.append(item)
            return self.show()
        curIdx = 1
        curNode = self.head
        newNode = Node(item)
        while True:
            curNode = curNode.next
            if curIdx == index:
                newNode.next = curNode.next
                curNode.next = newNode
                return newNode.item
            curIdx += 1

    def appendHead(self, item):
        newNode = Node(item)
        newNode.next =  self.head.next
        newHead = Node()
        newHead.next = newNode
        newNode.prev = newHead
        self.head = newHead

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def erase(self, index):
        if index >= self.lenght():
            return None
        curIdx = 0
        curNode = self.head
        while True:
            lastNode = curNode
            curNode = curNode.next
            if curIdx == index:
                lastNode.next = curNode.next
                return
            curIdx += 1

    def search(self, item):
        cur = self.head
        inx = 0
        while cur.next is not None:
            cur = cur.next
            if cur.item == item:
                return inx
            inx += 1

    def shifL(self):
        inx = self.search('|')
        if inx != 0 :
            self.erase(inx)
            self.insert(inx - 1, '|')

    def shiftR(self):
        inx = self.search('|')
        if inx != self.lenght()-1 :
            self.erase(inx) 
            self.insert(inx + 1,'|')

inp = input('Enter Input : ').split(',')
L = LinkedList()
L.append('|')

for txt in inp:
    txt = txt.strip().split()
    typ = txt[0]
    #word = txt[1]
    if typ == 'I':
        L.insert(L.search('|'), txt[1])
    elif typ == 'L':
        L.shifL()
    elif typ == 'R':
        L.shiftR()
    elif typ == 'B':
        inx = L.search('|')
        if inx != 0:
            L.erase(inx-1)
    elif typ == 'D':
        inx = L.search('|')
        if inx != L.lenght()-1: 
            L.erase(inx+1)
print(L)