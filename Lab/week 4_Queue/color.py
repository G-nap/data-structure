for j in Inp[1]:
    MR.append(j)
    if len(MR) > 2:
        if MR[-1] == MR[-2] and MR[-2] == MR[-3]:
            left.append(j)
            for m in range(3):
                MR.pop()
            explode2 +=1

if left == ['B', 'A', 'C']:
    for o in range(3):
        left.pop()
    left.append('A')
    left.append('B')
    left.append('C')

for i in Inp[0]:
    NM.append(i)
    if len(NM) > 2:
        if NM[-1] == NM[-2] and NM[-2] == NM[-3]:
            if left != []:
                NM.insert(-1, str(left[-1]))
                left.pop(-1)
                if len(NM) > 3:
                    if NM[-1] == NM[-2] and NM[-2] == NM[-3]:
                        for k in range(3):
                            NM.pop()
                        failed +=1
            else:
                for k in range(3):
                    NM.pop()
                explode1 +=1

print('NORMAL : ')
print(len(NM))
if len(NM) == 0:
    print('Empty',end='')
else:
    for l in range(len(NM)):
        print(NM[len(NM)-1-l],end='')
print('\n' + str(explode1) + ' Explosive(s) ! ! ! (NORMAL)')
if failed != 0:
    print('Failed Interrupted ' + str(failed) + ' Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(len(MR))
if len(MR) == 0:
    print('ytpmE', end='')
else:
    for n in range(len(MR)):
        print(MR[0],end='')
        MR.pop(0)
print('\n(RORRIM) ! ! ! (s)evisolpxE ' + str(explode2))