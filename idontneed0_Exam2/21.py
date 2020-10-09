def ans(li):
  if len(li) == 0:
    return 'Empty'
  return ", ".join(li)

inp = input('Enter Input : ').split(',')
s = []
d = []
for e in inp:
  txt = e.split()
  typ = txt[0]
  if typ == 'D':
    if len(s) == 0:
      print('Empty')
    else:
      p = s.pop(0)
      d.append(p)
      print(p,'<-', ans(s))
  elif typ == 'E':
    s.append(txt[1])
    print(ans(s))

print(ans(s), ":", ans(d))
  
  