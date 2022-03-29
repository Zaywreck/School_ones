from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Adınızı girin: ")

def fonk():
    x = "ananı sikeyim " + e.get()
    satır1 = Label(root, text=x).pack()


tus = Button(root, text="Adını yaz", command=fonk, fg="black", bg="red").pack()
    

root.mainloop()
