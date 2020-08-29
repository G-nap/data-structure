print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
x = num+(3*(num-1))
for i in range(1,int((x+1))) :
    if  i <=  (num*2)-1 :
        if i == 1 :
            print("#"*x)
        elif i%2 == 0 :
            print("#."*int(i/2)+"."*(x-(2*(i)))+".#"*int(i/2))
        elif i%2 == 1 :
            print("#."*int(i/2)+"#"*(x-(4*(int(i/2))))+".#"*int(i/2))
        elif i == (num*2)-1 :
            print("#."*(i-(i+1))+"#"+".#"*(i-(i+1)))
    if i > (num*2)-1 :
        if i%2 == 0 :
            print("#."*((int((x-i)/2))+1)+"."*(((2*i)-x)-2)+".#"*((int((x-i)/2))+1))  
        elif i == x :
            print("#"*x)
        elif i%2 == 1 :
            print("#."*((int((x-i)/2)))+"#"*(((2*i)-x))+".#"*((int((x-i)/2))))  