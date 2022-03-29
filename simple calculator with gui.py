from tkinter import *

root = Tk()
root.title("Hesap makinesi")

e = Entry(root, width=35, borderwidth=5).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add():
    return

tus_1 = Button(root, text="1", padx=30, pady=15, command=button_add)
tus_2 = Button(root, text="2", padx=30, pady=15, command=button_add)
tus_3 = Button(root, text="3", padx=30, pady=15, command=button_add)
tus_4 = Button(root, text="4", padx=30, pady=15, command=button_add)
tus_5 = Button(root, text="5", padx=30, pady=15, command=button_add)
tus_6 = Button(root, text="6", padx=30, pady=15, command=button_add)
tus_7 = Button(root, text="7", padx=30, pady=15, command=button_add)
tus_8 = Button(root, text="8", padx=30, pady=15, command=button_add)
tus_9 = Button(root, text="9", padx=30, pady=15, command=button_add)
tus_0 = Button(root, text="0", padx=30, pady=15, command=button_add)

#ekrana koyma

tus_7.grid(row=1, column=1)
tus_8.grid(row=1, column=2)
tus_9.grid(row=1, column=3)
tus_4.grid(row=2, column=1)
tus_5.grid(row=2, column=2)
tus_6.grid(row=2, column=3)
tus_1.grid(row=3, column=1)
tus_2.grid(row=3, column=2)
tus_3.grid(row=3, column=3)




root.mainloop()
