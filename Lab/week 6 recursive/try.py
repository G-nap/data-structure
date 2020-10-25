total = 1
def recurtion(x):  
  global total
  print(str(x),end="")
  if x > 1:
    total *= x
    x -= 1
    print(" x ",end="")
    recurtion(x)
 
  
  
x = input("Enter : ")
print(str(x) + "! = ",end="")
recurtion(int(x))
print(" =","{:,}".format(total))