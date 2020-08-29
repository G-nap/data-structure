print(" *** Perfect Number Verification ***")
n = input("Enter number : ")
num = int(n)
fac = []
sum = 0

if num > 0 :
    for i in range(1,num) :
        if num % i ==0 :
            fac.append(i)
    for e in fac :
        sum += e
    if num == sum :
        print(num,"is a PERFECT NUMBER.")
        print("Factors :",fac)
    else :
        print(num,"is NOT a perfect number.")
        print("Factors :",fac)
else :
    print("Only positive number !!!")