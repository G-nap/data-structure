print("*** String Rotation ***")
txt1,txt2 = input("Enter 2 strings : ").split()
txt1_st = txt1[0]
txt2_st = txt2[0]
i = 2
j = -3
count = 1
"""
def rotate(l, x):
  return l[-x:] + l[:-x]
"""
def rotate(li,x) :
  return li[-x % len(li):] + li[:-x % len(li)]

while count > 0 :
  rotate_txt1 = rotate(txt1,i)
  rotateTxt1_st = rotate_txt1[0]

  rotate_txt2 = rotate(txt2,j)
  rotateTxt2_st = rotate_txt2[0]
  
  #print("-------->",txt1_st,rotate_txt1[0])
  if txt1_st == rotate_txt1[0] and txt2_st == rotate_txt2[0]:
    print(" . . . . . ")
    print(count,rotate_txt1,rotate_txt2)
    print(f"Total of  {count} rounds.")
    break
  if count <= 5 :
    print(count,rotate_txt1,rotate_txt2)
  i += 2
  j -= 3
  count += 1
  
