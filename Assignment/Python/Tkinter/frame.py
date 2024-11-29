from tkinter import *



root = Tk()
root.title("My GUI")

root.geometry("926x526")

f1 = Frame(root, bg="Grey", borderwidth=10, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

l1 = Label(f1, text="Normal VS Code.")
l1.pack(pady=230)

f2 = Frame(root, bg="Grey", borderwidth=10, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l2 = Label(f2, text="Welcome to Tkinter Menu", font="helvetica 15 bold", fg="red")
l2.pack()



root.mainloop()