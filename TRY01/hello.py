"""
print("Hello")
print(10)
print("3.14") #string
print(3.14) 

print("5"+"5") #55

if 5>4:
    print("Yes !");
"""
customer_list = ["Chotika","Kititee","Vorakan"]
"""
print("Hello " + customer_list[0])
print("Hello " + customer_list[1])
print("Hello " + customer_list[2])
"""

def sayHello() :
    print("Hello")

customer = []
def inputAddUser(round) :
    for j in range(round) :
        customer.append(input("customer name "+str(j)+": "))

def showHelloAllUser() :
    for data in customer :
        print("Hello "+data)

for item in customer_list :
    print("Hello " + item)

for index in range(10) :
    print(index)

user_input = int(input("Enter input : "))
for i in range(user_input) :
    print("*"*(i+1))


customer_input = int(input(" : ")) #จำนวนรอบ
inputAddUser(customer_input)
showHelloAllUser()