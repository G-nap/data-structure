def lookBack(s):
  if s.index(max(s)) > 0:
    for i in range(s.index(max(s))-1,-1,-1):
      if s[i] <= max(s):
        s.pop(i)
        
  print(len(s), s)

def venom(s, combo):
  for i in range(len(s)):
    if s[i] % 2 == 0:
      s[i] -= 1*combo
    elif s[i] % 2 == 1:
      s[i] += 2*combo


inp = input("Enter : ").split(',')
s = []
combo = 0

for e in inp:
  txt = e.split()
  typ = txt[0]
  if typ == 'A':
    s.append(int(txt[1]))
    print('List :',s)
  elif typ == 'S':
    combo += 1
    venom(s, combo)
    print('Venom :',s)
  elif typ == 'B':
    combo = 0
    lookBack(s)
    