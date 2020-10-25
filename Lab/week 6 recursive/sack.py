def printSack(path, maxi):
  global arr
  global count
  count += 1
  for i in range(maxi+1):
    print(arr[path[i]], end = ' ')
  print()

def pantip(path, i, k, n):
  global N
  global arr

  if n< N:    # have something left to pick
    price = arr[n]    # good-price

    if k < price:   # cannot afford that ig
      pantip(path, i, k, n+1) # try to pick next good
    else:               # can buy
      k -= price  # pay
      path[i] = n # pick that ig to the sack at i

      if k == 0:  # done
        printSack(path, i)
      else:           # still have moneyLeft
        pantip(path, i+1, k, n+1)
        
      pantip(path, i, k+price, n+1)  # take the item off the sack for other solutions 
  return count


inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
N = len(arr)   # numbers of good
path = N*[-1]   # empty sack
k = int(inp[0])      # money left
i = 0           # sack index
n = 0          # good index
count = 0
pattern = pantip(path, i, k,n)
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))