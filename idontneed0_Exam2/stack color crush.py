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

  def reversed_display(self):
    if self.isEmpty():
      return 'Empty'
    return "".join(str(e) for e in reversed(self.items))

  def boomz(self):
    return self.items[-1] == self.items[-2] == self.items[-3]

inp = input('Enter Input : ').split()
s = Stack()
combo = 0

for e in inp:
  s.push(e)
  if s.size() > 2:
    if s.boomz():
      combo += 1
      for i in range(3):
        s.pop()

print(s.size())
print(s.reversed_display())
if combo > 1:
  print(f"Combo : {combo} !!!")