class MyInt():
    def __init__(self,x):
        self.x = x

    def isPrime(self):
        if self.x % 2 != 0 and self.x % 3 != 0 and self.x % 5 != 0 and self.x % 7 != 0:
            return f"{self.x} isPrime : True"
        else :
            return f"{self.x} isPrime : Fault"

    def showPrime(self):
        lst = []
        for i in range(2,self.x+1) :
            if i == 2 :
                lst.append(i)
            elif i < 9 and i % 2 != 0:
                lst.append(i)
            elif self.x %i != 0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 :
                lst.append(i)
            elif i == self.x and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 :
                lst.append(i)
        lst = [str(e) for e in lst]
        lst = " ".join(lst)
        return f"Prime number between 2 and {self.x} : {lst}"
         
    def __sub__(self,rhs):
        return  f"{self.x} - {rhs.x} = {self.x - int(rhs.x/2)}"

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