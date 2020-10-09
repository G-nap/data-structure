class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = Node()

    def __str__(self):
        return " ".join(str(e) for e in self.show())

    def reverse(self):
        return " ".join(str(e) for e in reversed(self.show()))

    def append(self, item):
        newNode = Node(item)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode

    def isEmpty(self):
        return self.head.next == None
    
    def show(self):
        li = []
        cur =  self.head
        while cur.next is not None:
            cur = cur.next
            li.append(cur.item)
        return li

def Linked(li):
    linkedList = LinkedList()
    for item in li:
        linkedList.append(item)
    return linkedList

inp = input('Enter Input (L1,L2) : ').split()
    
L1 = inp[0].split('->')
L2 = inp[1].split('->')
linkedList_L1 = Linked(L1)
linkedList_L2 = Linked(L2)
print('L1    :',linkedList_L1)
print('L2    :',linkedList_L2)
print('Merge :',linkedList_L1,linkedList_L2.reverse()) 

        
    

