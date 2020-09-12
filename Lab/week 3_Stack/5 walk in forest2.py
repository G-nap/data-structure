n = input('Enter Input : ').split(',')
temp = []
h = []
pi = 0 
HCopy = []

for e in range(len(n)):
    s = n[e].split(' ')
    temp.append(s)

    if temp[e][0] == 'A':
        h.append(float(temp[e][1]))   

    elif temp[e][0] == 'B':
        HCopy = [j for j in h]      
          
        for l in range(len(HCopy)):
            if HCopy[l]% 2 == 0:
                HCopy[l] -= 1*pi        
                if HCopy[l]< 1:
                    HCopy[l] = 1
            elif HCopy[l]%2==1:
                HCopy[l]+= 2*pi

        if len(HCopy) != 0:
            PN = len(HCopy)-1
            while PN > 0:
                PO = PN - 1
                while PO >= 0:
                    if HCopy[PN] >= HCopy[PO]:
                        HCopy.pop(PO)
                        PN -= 1
                    PO -= 1
                PN -= 1   
        pi = 0
        print(len(HCopy))
         

    

