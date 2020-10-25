def printPath(path, maxi):     
  global arr
  global i
  global count
  count += 1
  for i in range(maxi+1):
    print(f'[{i}]',arr[path[i]], end=' ')
  print()
  

def pantip(k, n, arr, path):
  global i
  global N

  if n < N:
    price = arr[n]
    if k < price: # 1. ถ้าเงินไม่พอซื้อ ให้ เลื่อนไปที่ของชิ้นถัดไป
      pantip(k, n+1, arr, path)

    else: # 2. ถ้าเงินพอซื้อ ให้ ซื้อ
      k -= price
      #path[i] = n
      path += [price]
    
      if k == 0: # 3. ถ้าตังหมด ให้ โชว์ว่าซื้อไรได้บ้าง
        print(path) 
        #print(path)
      else: # 4. ถ้าตังยังเหลือ ให้ เลื่อนไปที่ของชิ้นถัดไป
        pantip(k, n+1, arr, path) 
      pantip(k, n+1, arr, path)


  return count

 
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]

N = len(arr)

count = 0
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))
