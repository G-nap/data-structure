def lookBack(s):
  if s.index(max(s)) > 0:
    for i in range(s.index(max(s))-1,-1,-1):
      if s[i] <= max(s):
        s.pop(i)


inp = input("Enter : ").split(',')
s = []

for e in inp:
  txt = e.split()
  typ = txt[0]
  if typ == 'A':
    s.append(int(txt[1]))
  elif typ == 'B':
    lookBack(s)
    print(s)
      