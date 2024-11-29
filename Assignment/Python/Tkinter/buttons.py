from tkinter import *


root = Tk()
root.title("Buttons")

root.geometry("926x426")

def get_id():
    print("ID: 1")

def get_name():
    print("Name: Paras")

def get_surname():
    print("Surname: Rana")

def get_Language():
    print("Language: Python")

f1 = Frame(root, bg="light blue", borderwidth=10, relief=SUNKEN)
f1. pack(side=LEFT, anchor=NW, fill="x", expand=True)

b1 = Button(f1, fg="red", text="Get ID", command=get_id)
b1.pack(side=LEFT, padx=30)

b2 = Button(f1, fg="red", text="Get Name", command=get_name)
b2.pack(side=LEFT, padx=30)

b3 = Button(f1, fg="red", text="Get Surname", command=get_surname)
b3.pack(side=LEFT, padx=30)

b4 = Button(f1, fg="red", text="Get Language", command=get_Language)
b4.pack(side=LEFT, padx=30)


root.mainloop()