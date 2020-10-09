shelf,order = input('Enter Input : ').split('/')
order2 = order.split(',')
inShelf = []
inOrder = []
temp = []
order3 = []
#print(order2)

for n in range(len(order2)) :
    order3.append(order2[n].split())
#print(order3)

def hasNoDuplicates(lst):
    if len(lst) == len(set(lst)) and len(lst) >= 0:
        print('NO Duplicate')
    elif len(lst) != len(set(lst)) :
        print('Duplicate')


for book in shelf.split():
    if book != ' ':
        inShelf.append(book)

for e in range(len(order3)):
        if order3[e][0] == 'E':
            inShelf.append(order3[e][1]) 
        elif order3[e][0] == 'D':
            inShelf.pop(0)

hasNoDuplicates(inShelf)

#print('order',order)
#print('inOrder',inOrder)