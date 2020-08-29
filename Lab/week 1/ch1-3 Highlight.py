print("*** Reading E-Book ***")
text_input = input("Text , Highlight : ")
input_list = text_input.split(",")
#print(input_list)
text = list(input_list[0])
highlight = input_list[1]
#print(text)
#print(highlight)
for e in text :
    if e == highlight :
        print("["+e+"]",end="")
    else :
        print(e,end="")
