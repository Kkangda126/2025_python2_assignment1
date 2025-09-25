from tkinter import *

root = Tk()
photo = PhotoImage(file="kitten.png")
label = Label(root, image=photo)
label.pack()
root.mainloop()