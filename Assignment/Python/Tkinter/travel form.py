from tkinter import *

root = Tk()
root.title("My GUI - Travel Form")
root.geometry("1000x624")
root.minsize(725,24)

# Configure root grid layout
root.rowconfigure(0, weight=0)  # Header row
root.rowconfigure(1, weight=1)  # Main frame row
root.columnconfigure(0, weight=1)

# Header frame:
header_frame = Frame(root, bg="blue", height=20)
header_frame.grid(row=0, column=0, sticky=EW)

header_frame.rowconfigure(0, weight=1)
header_frame.columnconfigure(0, weight=1)

heading = Label(header_frame, text = "Welcome To Shubh Travels", font="cosmatic 20 bold", bg="blue", fg="black")#, padx=25, pady = 25)
heading.grid(row=0, column=0, sticky=NSEW)

# Main frame:
main_frame = Frame(root, bg="light blue")
main_frame.grid(row=1, column=0, sticky=NSEW)

# Configure grid layout in main frame
main_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
main_frame.columnconfigure((0, 1, 2), weight=1)

# Details label
name = Label(main_frame, text="Name: ")
age = Label(main_frame, text="Age: ")
gender = Label(main_frame, text="Geder: ")
phone = Label(main_frame, text="Phone No: ")
payment_mode = Label(main_frame, text="Payment Mode: ")

name.grid(row=1, column=2)
age.grid(row=2, column=2)
gender.grid(row=3, column=2)
phone.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

# Details variable
name_value = StringVar()
age_value = StringVar()
gender_value = StringVar()
phone_value = StringVar()
payment_mode_value = StringVar()
food_service_value = IntVar()

# Detail entries
name_entry = Entry(main_frame, textvariable=name_value)
age_entry = Entry(main_frame, textvariable=age_value)
gender_entry = Entry(main_frame, textvariable=gender_value)
phone_entry = Entry(main_frame, textvariable=phone_value)
payment_mode_entry = Entry(main_frame, textvariable=payment_mode)
food_service_entry = Entry(main_frame,textvariable=food_service_value)

name_entry.grid(row=1, column=2)
age_entry.grid(row=2, column=2)
gender_entry.grid(row=3, column=2)
phone_entry.grid(row=4, column=2)
payment_mode_entry.grid(row=5, column=2)

Button(root, text="Submit", bg="light green", font="helvetica 10 bold", fg="black").grid(row=9, column=3)


root.mainloop()