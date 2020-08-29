import tkinter as tk                        # Tkinter = Library สำหรับสร้าง  GUI (Desktop App)

def set_message():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()                            #สร้างหน้าต่าง
window.title('JustPython')
window.minsize(width=400,height=400)

######### UI (user interface)

title_label = tk.Label(master=window, text='Hello World')      # Label ข้อความ , master เป็นตัวบอกว่าจะไปใส่ไว้ที่ไหน ในที่นี้คือ window
title_label.pack()                                              # pack ตรงกลาง

text_input = tk.Entry(master=window)                            # Entry ช่องกรอกข้อความ
text_input.pack()

ok_button = tk.Button(master=window, text='okay', command=set_message)
ok_button.pack()

###########

window.mainloop()                           # Start App