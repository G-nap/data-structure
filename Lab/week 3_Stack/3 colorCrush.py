"""
-------------------------------
Enter Input : G H H H H P
3
PHG
-------------------------------
Enter Input : L C C X X X C D
2
DL
Combo : 2 ! ! !
-------------------------------
Enter Input : C C C
0
Empty
-------------------------------
"""
n = input('Enter Input : ').split()
stack = []
combo = 0
for e in n:
    stack.append(e)
    if len(stack) > 2:
        if stack[-1] == stack[-2] and stack[-2] == stack[-3]:
            stack.pop()
            stack.pop()
            stack.pop()
            combo += 1
stack.reverse()
print(len(stack))
if len(stack) == 0:
    print('Empty')
else:
    print(''.join(stack))
if combo > 1 :
    print(f'Combo : {combo} ! ! !')