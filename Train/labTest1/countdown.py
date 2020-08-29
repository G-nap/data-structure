print("*** Fun with countdown ***  ")
num = [int(e) for e in input("Enter List : ").split()]
count = 0
temp = []
countdown =[[]]
for i in range(len(num)) :
    if num[i] != 1 :
        if num[i] - num[i+1] == 1 :
            temp.append(num[i])
        else :
            teme = []
    if num[i] == 1 :
        temp.append(num[i])
        count += 1
        countdown[0].append(temp)
        temp =[]
countdown.insert(0,count)
print(countdown)