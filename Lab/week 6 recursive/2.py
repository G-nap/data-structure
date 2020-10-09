lst = []
def Sort(i,inp):
  global lst
  if i < len(inp):
    x = int(inp[i])
    lst.append(x)
    i+=1
    return Sort(i,inp)
  else:
    lst.sort()
    lst.reverse()
    print("List after Sorted :",lst)

inp = input("Enter your List : ").split(',')
Sort(0,inp)