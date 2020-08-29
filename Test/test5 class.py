class MyInt():
    def __init__(self,num):
        self.num = num

    def isPrime(self):
        if self.num %2 != 0 :
            return f"{self.num} isPrime : True"
        return f"{self.num} isPrime : False"

    def showPrime(self):
        if self.num > 2 :
            lst = []
            for i in range(2,self.num+1) :
                #print(i)
                if i == 2 :
                        lst.append(i)
                elif i == self.num and i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
                        lst.append(i)
                elif i >= 9 :
                    if self.num % i != 0 and i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 :
                        lst.append(i)
                else :
                    if self.num % i != 0 and i%2 != 0 or i%5 == 0:
                        lst.append(i)
            lst = [str(e) for e in lst]
            lst = ' '.join(lst)
            return f"Prime number between 2 and {self.num} : {lst}"
        return f"Prime number between 2 and {self.num} : !!!A prime number is a natural number greater than 1"

    def __sub__(self,rhs):
        return f"{self.num} - {rhs.num} = {self.num - int(rhs.num/2)}"

print(" *** class MyInt ***")
print("Enter 2 number : ",end="")
x,y = input().split()
a = MyInt(int(x))
b = MyInt(int(y))
print(a.isPrime())
print(b.isPrime())
print(a.showPrime())
print(b.showPrime())
print(a-b)



