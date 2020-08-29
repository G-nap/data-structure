txt = input("Enter : ")
txtDict = {}
txtList = []
count = 0
for e in txt :
    if e not in txtDict :
        txtDict[e] = count
        count += 1
for e in txt :
    txtList.append(txtDict[e])
print(txtList)