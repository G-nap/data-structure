"""

1. bubble sort /
2. selection sort /
3. insertion sort /
4. shell sort
5. heap sort
6. merge sort
7. quick sort

"""

def bubbleSort(arr): 
  size = len(arr)
  for i in range(size):
    for j in range(0, size-i-1):
      if arr[j] > arr[j+1] : 
        arr[j],arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):
  size = len(arr)
  for step in range(size):
    min_idx = step
    for i in range(step+1, size): 
      if arr[i] > arr[min_idx]:
        min_idx = i
    arr[step], arr[min_idx] = arr[min_idx], arr[step]

def insertionSort(arr):
  size = len(arr)
  for i in range(1, size):
    key = arr[i]
    while j >= 0 and key < arr[j] :
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key


        

#inp = [int(i) for i in input('Enter Input : ').split()]
inp = [64, 25, 12, 22, 11 , 33]  # 11 12 22 25 64 
insertionSort(inp)
for i in range(len(inp)):
  print('%d' %inp[i],end =" ")
