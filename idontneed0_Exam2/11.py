class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]

  def isEmpty(self):
    return self.items == []

  def size(self):
    return len(self.items)

def match(op, cl):
  openn = '([{'
  close = ')]}'
  return openn.index(op) == close.index(cl)

inp = input('Enter Input : ')
inp = list(inp)
s = Stack()

for e in inp:
  if e in '([{':
    s.push(e)
  elif e in ')]}':
    if match( s.pop(), e):
      print('Match !!!')
    else:
      print('NOT Match !!!')