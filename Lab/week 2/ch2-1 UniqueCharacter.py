txt = input("Enter String : ")
txtList = []
txtDict = {}
num = 0
for e in txt :
    if e not in txtDict :
        txtDict[e] = num
        num+=1
for e in txt :
    txtList.append(txtDict[e])
print(txtList)

