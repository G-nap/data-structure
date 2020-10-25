lst = []
i = 0
tmp = 0
def sort_maxTomin(i, lst): 
  global lst
  if len(lst) != 0:
    if i == 0:
      tmp = int(lst[0])
    if i < len(lst):
      if int(lst[i]) > tmp:
        tmp = int(lst[i])
      





inp = input('Enter your List : ').split(',')