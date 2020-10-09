class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def match(o,c):
    openn = '([{'
    close = ')]}'
    return openn.index(o) == close.index(c)

inp = input('Enter input : ')
inp = list(inp)
s = Stack()
error = 0

for e in inp:
    if e in '([{':
        s.push(e)
    elif e in ')]}':
        if s.size() > 0 :
            if match(s.pop(), e):
                error = 1
            else:
                error = 2
if s.size() > 0:
    error = 3

if error == 1 :
    print('Match !!!')
elif error == 2 :
    print('Not Match !!!')