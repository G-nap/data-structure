num = [int(e) for e in input("Enter number end with (-1) : ").split()]
lst = []

if -1 not in num :
    print("Invalid INPUT !!!")
else :
    for e in num :
        if e == -1 :
            break
        elif e != -1 :
            lst.append(e)   



    if len(lst) == 0 :
        print("Not found")


    else :
        d = {x:lst.count(x) for x in lst}
        maxValue = max(d.values())
        maxValueList =[k for k, v in d.items() if v == maxValue]
        if (len(maxValueList)>1) :
            print("Not found")
        else :
            print(maxValueList[0])

