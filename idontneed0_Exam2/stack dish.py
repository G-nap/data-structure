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

  def __str__(self):
    return str(self.items)

inp = input('Enter Input : ').split(',')
s = Stack()

for e in inp:
  w,f = e.split()
  if s.size() > 0 and int(s.peek()[0]) < int(w):
    print(s.pop()[1])
    while s.size() > 0 and int(s.peek()[0]) < int(w):
      print(s.pop()[1])
  s.push((w,f))