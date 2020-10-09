min = 0
def Min(i,num):
  global min
  if i == 0:
    min = int(num[0])
  if i < len(num):
    if min < int(num[i]):
      min = min
    else:
      min = int(num[i])
    i += 1
    Min(i,num)
  else:
    print("Min :",min)

num = input("Enter Input : ").split()
Min(0,num)