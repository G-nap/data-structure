print('*** Converting hh.mm.ss to seconds ***')
print('Enter hh mm ss : ',end = "")
h,m,s = [int(e) for e in input().split()]

if h > 59 or h <0:
    print("mm(",m,")"," is invalid!",sep="")
elif m > 59 or m <0:
    print("mm(",m,")"," is invalid!",sep="")
elif s > 59 or s <0:
    print("mm(",m,")"," is invalid!",sep="")

else:
    print("{:02}:{:02}:{:02} = {:,}".format(h,m,s,h*60*60+m*60+s),"seconds")

