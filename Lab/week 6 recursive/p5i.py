sum = 0
def pantip(k, n, arr, path):
  global sum
  if n < len(arr):
   
    if k < arr[n]:
      pantip(k, n+1, arr, path)
    else:
      k -= arr[n]
      path += [arr[n]]
      if k == 0:
        print(path)
      else: 
        pantip(k, n+1, arr, path)
      pantip(k, n+1, arr, path)


  return len(path)

  



inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]

pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))
