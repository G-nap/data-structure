txt = input('Enter Input : ').split(',')
#print(txt)
newTxt = []
Q = []
P = []
for e in range(len(txt)) :
    newTxt.append(txt[e].split())
    typ = newTxt[e][0]
    if typ == 'E' :
        Q.append(newTxt[e][1])
        print(', '.join(Q))
    elif typ == 'D':
        #Q.pop(0)
        if len(Q) == 0:
            print('Empty')  
        else:
            p = Q.pop(0)
            P.append(p) 
            if len(Q) == 0:
                print(p,'<-','Empty')
            else:
                print(p,'<-',', '.join(Q))
                
if len(P) == 0 and len(Q) == 0:
    print('Empty',':','Empty')
elif len(Q) == 0:
    print(', '.join(P),':','Empty')
elif len(P) == 0:
    print('Empty',':',', '.join(Q))
else:
    print(', '.join(P),':',', '.join(Q))
#print(newTxt)
