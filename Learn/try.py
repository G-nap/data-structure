def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
      if arr[j+1] < arr[j]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):
  for i in range(len(arr)):
    minn = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[minn]:
        minn = i
    arr[i], arr[minn] = arr[minn], arr[i]

def insertSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key



inp = [9,8,6,5,3,1,7,2,4]
selectionSort(inp)
for i in inp:
  print(i, end =" ")