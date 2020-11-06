def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr)-1):
      if arr[j+1] < arr[j]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion(arr):
  for i in range(len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key > arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

inp = [int(i) for i in input('Enter : ').split()]
insertion(inp)
for i in range(len(inp)):
  print(inp[i], end = " ")