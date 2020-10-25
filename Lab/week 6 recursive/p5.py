sum = 0

def pantip(k, n, arr, path):
  global sum
  if n < len(arr):
    print(arr[n],end=" ")
    sum += arr[n]
    if sum == k:
      print(f"[{sum}]")
      sum = 0
    if sum != k:
      print(arr[n])
      pantip(k, n, arr, path)
      n += 1


inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("")
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))
