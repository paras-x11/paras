from tkinter import *

def my_func():
    print("Hello, Paras")

root = Tk()

root.geometry("500x450")
root.title("My GUI - Menus")

menubar = Menu(root)

m1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=m1)

m1.add_command(label="New File", command=my_func)
m1.add_separator()
m1.add_command(label="Save", command=my_func)
m1.add_command(label="Save As", command=my_func)
m1.add_separator()
m1.add_command(label="Print", command=my_func)

root.configure(menu=menubar)


m2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=m2)

m2.add_command(label="Undo", command=my_func)
m2.add_command(label="Redo", command=my_func)
m2.add_separator()
m2.add_command(label="Cut", command=my_func)
m2.add_command(label="Copy", command=my_func)
m2.add_command(label="Paste", command=my_func)

root.configure(menu=menubar)

root.mainloop()
