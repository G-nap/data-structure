min = 0
i = 0
def find_min(i):
  global min #
  if i == 0:
    min = int(li[i]) #int
  if i < len(li): #elif
    if int(li[i]) < min: #int
      min = int(li[i]) #int
    else:
      min = min
    i += 1
    find_min(i)
  else:
    print(min)

li = input("Enter : ").split() #wrong spilt()
find_min(i)


