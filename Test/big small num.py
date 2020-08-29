txt = input("Enter : ")
big = 0
small = 0
num = 0
for e in txt :
    if 'A' <= e <= 'Z' :
        big += 1
    elif 'a' <= e <= 'z':
        small += 1
    elif '1' <= e <= '9' :
        num += 1
maxV = max(big,small,num)
if big == maxV :
    print("big :",maxV)
elif small == maxV :
    print("small :",maxV)
elif num == maxV :
    print("num :",maxV)