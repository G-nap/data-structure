r,o = input('Enter Input : ').split('/')
#print(r)
#print(o)
row = r.split(',')
order = o.split(',')
#print(row)
#print(order)
inRow = []
inOder = []
Q = []
mem = {}

for i in range(len(row)):
    inRow.append(row[i].split())
    
for i in range(len(inRow)):
    dpmt = inRow[i][0]
    ID = inRow[i][1]
    mem[ID] = dpmt

print('mem',mem)


for i in range(len(order)):
    inOder.append(order[i].split())
#print(inOder)

for i in range(len(inOder)):
    typ = inOder[i][0]
    if typ == 'E' and inOder[i][1] in mem.keys():
        Q.append(inOder[i][1])
    
    elif typ == 'D':
        if len(Q) > 0:
            #Q.sort()
            print(Q.pop(0))  
        else:
            print('Empty')

#print('------------------')
#print(Q)
#print(inRow)
#print(inOder)