txt = input('Enter Input : ').split(',')
newTxt = []
QEN = []
QES = []
for e in range(len(txt)):   
    newTxt.append(txt[e].split())
    typ = newTxt[e][0]
    if typ == 'EN':
        QEN.append(newTxt[e][1])
    elif typ == 'ES':
        QES.append(newTxt[e][1])
    else:
        if len(QES) == 0 and len(QEN) == 0:
            print('Empty')
        elif len(QES) != 0:
            print(QES.pop(0))
        else:
            print(QEN.pop(0))
        