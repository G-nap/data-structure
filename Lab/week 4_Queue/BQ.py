txt = input('Enter Input : ').split(',')
newTxt = []
q = []
a = len(q)
for i in range(len(txt)):
    newTxt.append(txt[i].split())
    typ = newTxt[i][0]
    if typ == 'E':
        q.append(newTxt[i][1])
        print(f'Add {newTxt[i][1]} index is {q.index(newTxt[i][1])}')
    elif typ == 'D':
        if len(q) == 0 :
            print(-1)
        else:
            print(f'Pop {q.pop(0)} size in queue is {len(q)}')

if len(q) == 0 :
    print('Empty')
else:
    print('Number in Queue is : ',q)
