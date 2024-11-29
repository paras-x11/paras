import os 
from tkinter import *

os.chdir("D:\\paras\\Assignment\\Python\\Tkinter")

root = Tk()
root.title("My GUI")
root.geometry("1000x624")
root.minsize(725,24)

name = Label(text = "Name: Kakashi Hatake")
name.pack(pady = 25)

photo = PhotoImage(file= "kakashi.png")
l2 = Label(image= photo, bg="light blue")
l2.pack(pady = 20)

title = Label(text = '''Kakashi Hatake (Japanese: はたけ カカシ, Hepburn: Hatake Kakashi) is a fictional character and one of the main protagonists \nin the Naruto manga and anime series created by Masashi Kishimoto. In the story, Kakashi is the teacher of Team 7, consisting of the series' \nprimary characters, Naruto Uzumaki, Sasuke Uchiha, and Sakura Haruno. Kakashi's past has been extensively explored in the series, resulting in a \ngaiden being devoted to his past experiences. Kakashi has appeared in several pieces of Naruto media, the featured films in the series, the \noriginal video animations, and the video games.''', bg = "light blue", padx = 90, pady = 70, font = "comicsansms 10 bold", borderwidth=5, relief=FLAT)

title.pack(side=TOP, anchor=N, padx=25, pady=25, fill=X)


root.mainloop()


# Important Lable Attributes
# 1. text  : Label text (e.g.,  text="Hello" ).  
# 2. image  : Displays an image ( image=photo_image ).  
# 3. font  : Sets text font (e.g.,  font=("Arial", 16, "bold") or font = "comicsansms 10 bold").  
# 4. fg  /  bg  : Text/Background colors ( fg="blue" ,  bg="yellow" ).  
# 5. width  /  height  : Dimensions in text units ( width=20 ,  height=5 ).  
# 6. anchor  : Aligns content (e.g.,  anchor="w" ).  
# 7. relief  : Border style ( flat ,  raised , SUNKEN, RAISED, GROOVE, RIDGE etc.).  
# 8. bd  : Border width ( bd=2 ).  
# 9. padx  /  pady  : Internal padding ( padx=10 ,  pady=5 ).  
# 10. justify   : Aligns multi-line text ( left ,  center ,  right ).  
# 11. wraplength  : Wraps text beyond given width (pixels).  
# 12. state     : Widget state ( normal ,  disabled ).  
# 13. cursor    : Changes cursor on hover (e.g.,  cursor="hand2" ).  
# 14. compound  : Combines text & image ( top ,  bottom , etc.). 


# pack: 
# 1. side : Position widget (top, bottom, left, right), e.g.,  side="left" .  
# 2. fill : Expand widget to fill space (none, x, y, both), e.g.,  fill="x" .  
# 3. expand : Use extra space if available (True/False), e.g.,  expand=True .  
# 4. padx : Horizontal external padding, e.g.,  padx=10 .  
# 5. pady : Vertical external padding, e.g.,  pady=5 .  
# 6. ipadx : Internal horizontal padding, e.g.,  ipadx=5 .  
# 7. ipady : Internal vertical padding, e.g.,  ipady=3 .  
# 8. anchor : Align widget (n, ne, e, etc.), e.g.,  anchor="w" .