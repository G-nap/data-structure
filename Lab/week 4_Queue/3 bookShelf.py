txt = input('Enter Input : ')

def hasNoDuplicates(lst):
        if len(lst) == len(set(lst)):
            return f'NO Duplicate'
        return f'Duplicate'

if '/' not in txt:
    txt = [e for e in txt if e != ' ' and e != ',' and e != 'E'] 
    for e in range(len(txt)) :
        if e == 'D':
            txt.pop(0)
    print(txt)
    #print('TT')   
    print(hasNoDuplicates(txt)) 
else:
    #print('yeahhhhh')

    shelf,order = txt.split('/')
    inShelf = []
    inOrder = []
    
    for book in shelf:
        if book != ' ':
            inShelf.append(book)

    for e in range(len(order)):
        if order[e] != ' ' and order[e] != ',':
            inOrder.append(order[e])
            if order[e] == 'E':
                inShelf.append(order[e+2]) #?
            elif order[e] == 'D':
                inShelf.pop(0)

    print(hasNoDuplicates(inShelf))

    #print('shelf',shelf)
    #print('inShelf',inShelf)
    #print('order',order)
    #print('inOrder',inOrder)