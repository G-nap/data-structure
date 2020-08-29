print(" *** BMI ***")
w,h = input("Enter your weight(kg) and height(m) : ").split()
weight = int(w)
hight = float(h)
BMI = weight/(hight*hight)
if BMI < 18.5 :
    print("Your status is : Below normal weight.")
elif 18.5 <= BMI < 25 :
    print("Your status is : Normal weight.")
elif 25 <= BMI < 30 :
    print("Your status is : Overweight.")
elif 30 <= BMI < 35 :
    print("Your status is : Case I Obesity.")
elif 35 <= BMI < 40 :
    print("Your status is : Case II Obesity.")
elif BMI >= 40 :
    print("Your status is : Case III Obesity.")