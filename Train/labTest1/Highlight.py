
print("*** Reading E-Book ***")
_input = input("Text , Highlight : ").split(",")
text = _input[0]
highlight =_input[1]
for cha in text :
    if cha == highlight :
        print(f"[{highlight}]",end="")
    else :
        print(cha,end="")
