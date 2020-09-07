n = input('Enter Input : ').split(',')
temp = []
h = []
for e in range(len(n)):
    s = n[e].split()
    temp.append(s)
    if temp[e][0] == 'A':
        h.append(int(temp[e][1]))
        #print(temp[e][1])
        #print(h[-1])
        
        #if len(h) > 1:
            #print(h[-1],h[-2])

        for i in range(len(h)-2,-1,-1):
            if h[-1] >= h[i]:
                h.pop(i)
            
            #if h[-1]>h[-2]:
                #print('pop',h.pop())
    elif temp[e][0] == 'B':
        print(len(h))
        
#print(temp)
#print(n)

