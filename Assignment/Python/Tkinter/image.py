import os
from tkinter import *

os.chdir("D:\\paras\\Assignment\\Python\\Tkinter")

root = Tk()

root.title("My GUI")

root.geometry("544x424")
root.minsize(444, 234)
root.maxsize(950, 700)

l1 = Label(text = "Hello, World!")
l1.pack()

photo =PhotoImage(file = "kakashi.png")
l2 = Label(image = photo)
l2.pack()





root.mainloop()