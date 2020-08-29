print("*** Converting hh.mm.ss to seconds ***")
h,m,s = [int(e) for e in input("Enter hh mm ss : ").split()]
if m > 59 or m <= 0 :
    print(f"m({m}) is invalid!")
else :
    print("{:02}:{:02}:{:02} = {:,}".format(h,m,s,h*3600+m*60+s),"seconds")

