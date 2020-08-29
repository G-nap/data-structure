def sumZero(x) :
    answer = []
    if len(x) <= 2 :
        return "Array Input Length Must More Than 2"
    for i in range(len(x)) :
        for j in range(i+1,len(x)) :
            for k in range(j+1,len(x)) :
                if x[i]+x[j]+x[k] == 0 and [x[i],x[j],x[k]] not in answer :
                    answer.append([x[i],x[j],x[k]])
    return answer
    
num = [int(e) for e in input("Enter Your List : ").split()]
print(sumZero(num))   