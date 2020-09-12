n = input('Enter Input (Normal, Mirror) : ').split()
#print(n)

nor = list(n[0])
mir = list(n[1])
stack_MIR = []
stack_NOR = []
boomz = []

def same(x,y,z):
    return x == y == z

for e in mir:
    stack_MIR.append(e)
    if len(stack_MIR) > 2:
        if stack_MIR[-1] == stack_MIR[-2] and stack_MIR[-2] == stack_MIR[-3]:
            for e in range(3):
                b = stack_MIR.pop()
            boomz.append(b)

print(boomz)

for i in range(len(nor)):
    stack_NOR.append(nor[i])

for i in range(len(stack_NOR)-2):
    if len(stack_NOR) > 2:
        if same(stack_NOR[i],stack_NOR[i+1],stack_NOR[i+2]):       # วางระเบิด
            if len(boomz) > 0:    
                stack_NOR.insert(i+2,boomz.pop())            
            else:
                stack_NOR.pop(i)
                stack_NOR.pop(i)
                stack_NOR.pop(i)
          
print(stack_NOR)




#############

print('NORMAL :')
print(len(stack_NOR))
if len(stack_NOR) == 0:
    print('Empty')
else:
    stack_NOR.reverse()
    print(''.join(stack_NOR))
print('xxx','Explosive(s) ! ! ! (NORMAL)')
print('------------MIRROR------------')
print(': RORRIM')
print(len(stack_MIR))
if len(stack_MIR) == 0:
    print('ytpmE')
else:
    print(''.join(stack_MIR))
print('(RORRIM) ! ! ! (s)evisolpxE','xxx')


#print(nor)
#print(mir)