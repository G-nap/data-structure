"""

1. bubble sort /
2. selection sort /
3. insertion sort /
4. shell sort 
5. heap sort
6. merge sort
7. quick sort

"""

def bubbleSort(arr): # Pair, if small swap to front
  size = len(arr)
  # Traverse through all array elements 
  for i in range(size):
     # Last i elements are already in place 
    for j in range(0, size-i-1):
      # traverse the array from 0 to n-i-1 
      # Swap if the element found is greater 
      # than the next elemen
      if arr[j] > arr[j+1] : ### change > or <
        arr[j],arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):  # min swap to first
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)): 
      # to sort in descending order, change > to < in this line
      # select the minimum element in each loop
      if arr[j] < arr[min_idx]: ### change > or <
        min_idx = i
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position 
    j = i-1
    while j >= 0 and key < arr[j] : ### change > or < (key)
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

def shellSort(l,dIncrements):
  for inc in dIncrements: #for each deminishing increment
    for i in range(inc, len(l)): #insertion sort
      iEle = l[i] #iserting element
      for j in range(i, -1, -inc):
        if iEle < l[j-inc] and j >= inc:
          l[j] = l[j-inc]
        else:
          l[j]  = iEle
          break
        

#inp = [int(i) for i in input('Enter Input : ').split()]
inp = [64, 25, 12, 22, 11 , 33] 
dIncrement = [5, 3, 2]

shellSort(inp, dIncrement)

for i in range(len(inp)):
  print('%d' %inp[i],end =" ")

# 11 12 22 25 64 