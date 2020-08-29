num = input("Enter number end with (-1) : ").split()
lst = []
if "-1" not in num :
    print("Wrong!!!")
else :
    for i in num :
        lst.append(i)
        if i == -1 :
            break

    if len(lst) <= 1 :
        print("not found")
    else:
        d = {x:lst.count(x) for x in lst}
        maxV = max(d.values())
        maxVl = [k for k , v in d.items() if v == maxV]

        if len(maxVl) > 1 :
            print("not found")
        else:
            print(maxVl[0])


