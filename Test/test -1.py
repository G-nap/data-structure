import operator
num = [int(e) for e in input("Enter number end with (-1) : ").split()]
lst = []

if -1 not in num :
        print("Invalid INPUT !!!")
else :
    for e in num : 
        if e == -1:
            break
        lst.append(e)
#print(lst)
    d = {x:lst.count(x) for x in lst}
#print(d)
#print(d.keys())
#print(d.values())

    maxD = max(d.items(), key=lambda x : x[1])
#print("Max Value : ",maxD[1])
#print("Max Key : ",maxD[0])
    print(maxD[0])