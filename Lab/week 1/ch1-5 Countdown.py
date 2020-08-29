print("*** Fun with countdown ***")
inputNum = input("Enter List : ")
numList = inputNum.split()
numList = [int(e) for e in numList]
count = 0
add = 0
countdown = 1
countdownList = [[]] 
i = 0
for e in numList :
    if numList[i] == 1 :
        count += 1
        countdownList[0].append([])
        gab = countdownList[0]
        addGab = gab[add]
        j = i
        while numList[j] == countdown :
            addGab.insert(0,numList[j])
            j-=1
            countdown+=1 
        add += 1
        countdown = 1
    i+=1
countdownList.insert(0,count)
print(countdownList)