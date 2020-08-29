txt = " n"
newtxt = ""

for i in txt :
    if not i in newtxt :
        newtxt += i        
print(newtxt)

#print(''.join(sorted(set(txt),reverse=True)))
