inp = input("Enter Input : ").split(',')
s = []

for e in inp:
  data = e.split()
  #print(data)
  typ = data[0]
  #print(data[0])
  if typ == 'A':
    s.append(int(data[1]))
    
  elif typ == 'B':
    for i in range(len(s)-2,-1,-1):
      if s[-1] >= s[i]:
        s.pop(i)
    print(s)