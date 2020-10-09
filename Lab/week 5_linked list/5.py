class Node():
    def __init__(self, item=None):
        self.item = item
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()

    def __str__(self):
        return " ".join(str(e) for e in self.show())

    def addList(self, item):
        self.head = Node()
        for e in item:
            self.append(e)

    def append(self, item):
        newNode = Node(item)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        newNode.perv = cur
        cur.next = newNode

    def show(self):
        li = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            li.append(cur.item)
        return li

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def sort(self):
        cur = self.show()
        li = []
        strList = []
        for e in cur:
            li.append(int(e))
        li = sorted(li)
        for e in li:
            strList.append(str(e))
        self.addList(strList)

def Digit(pos, item): 
    pos = pos*-1
    try:
        digit = item[pos]
        if digit != '-':
            return int(digit)  
        else:
            return 0
    except IndexError:
        return 0

def redixSort(li):
    round,inp = 0,len(li)
    subList = list(LinkedList() for e in range(10))

    while True:
        round += 1
        for i,item in enumerate(li):
            num = Digit(round,item)
            for j in range(10):
                if num == j:
                    subList[j].append(item)
                    break

        for i in range(10):
            subList[i].sort()
            
        print('------------------------------------------------------------')
        print('Round :',round)

        for i,item in enumerate(subList):
            print(f'{i} : {" ".join(item.show())}')
        li = []
        for i in subList:                               
            for j in i.show():
                li.append(j)
        if subList[0].lenght() == inp: break    
        subList = list(LinkedList() for e in range(10)) 
        
    return round-1,li

inp = input('Enter Input : ').split()
round,result = redixSort(inp)
print('------------------------------------------------------------')
print(round,'Time(s)')
print(f'Before Radix Sort : {" -> ".join(inp)}')
print(f'After  Radix Sort : {" -> ".join(result)}')