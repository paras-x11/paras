from tkinter import *
from tkinter import messagebox

class TravelFileHandler:
    def __init__(self, file_name="Travel_form.txt"):
        self.file_name = file_name

    def add_details(self, name, age, gender, phone, payment_mode, food_service):
        with open(self.file_name, "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Gender: {gender}\n")
            file.write(f"Phone No: {phone}\n")
            file.write(f"Payment Mode: {payment_mode}\n")
            file.write(f"Prebook Meals: {food_service}\n")
            file.write("-" * 30 + "\n")  # Add separator between entries
        print("Form data has been saved successfully!")

f = TravelFileHandler()

root = Tk()
root.title("My GUI - Travel Form")
root.geometry("600x500")
root.configure(bg="AliceBlue")  
root.minsize(525, 370)

# Configure root grid layout
root.rowconfigure(0, weight=0)  # Header row
root.rowconfigure(1, weight=1)  # Main frame row
root.columnconfigure(0, weight=1)

# Header frame 
header_frame = Frame(root, bg="Teal", borderwidth=5, relief=SUNKEN, height=20)
header_frame.grid(row=0, column=0, sticky=EW, padx=(20, 20), pady=(20, 0))

header_frame.rowconfigure(0, weight=1)
header_frame.columnconfigure(0, weight=1)

heading = Label(header_frame, text="Welcome To Travels Company", font="cosmic 20 bold", bg="Teal", fg="White", padx=5, pady=5)
heading.grid(row=0, column=0, sticky=NSEW)

# Main frame 
main_frame = Frame(root, bg="lightskyblue1", borderwidth=5, relief=GROOVE)  
main_frame.grid(row=1, column=0, sticky=NSEW, padx=(20, 20), pady=(0, 20))

# Details labels
name = Label(main_frame, text="Name: ", font="helvetica 9 bold", bg="CadetBlue", fg="White")
age = Label(main_frame, text="Age: ", font="helvetica 9 bold", bg="CadetBlue", fg="White")
gender = Label(main_frame, text="Gender: ", font="helvetica 9 bold", bg="CadetBlue", fg="White")
phone = Label(main_frame, text="Phone No: ", font="helvetica 9 bold", bg="CadetBlue", fg="White")
payment_mode = Label(main_frame, text="Payment Mode: ", font="helvetica 9 bold", bg="CadetBlue", fg="White") 

name.grid(row=0, column=0, sticky=W, padx=(20, 5), pady=(20, 5))
age.grid(row=1, column=0, sticky=W, padx=(20, 5), pady=5)
gender.grid(row=2, column=0, sticky=W, padx=(20, 5), pady=5)
phone.grid(row=3, column=0, sticky=W, padx=(20, 5), pady=5)
payment_mode.grid(row=4, column=0, sticky=W, padx=(20, 5), pady=5)

# Details variable
name_value = StringVar()
age_value = StringVar()
gender_value = StringVar()
phone_value = StringVar()
payment_mode_value = StringVar()
food_service_value = IntVar()

# Detail entries 
name_entry = Entry(main_frame, textvariable=name_value, bg="White", fg="Black")
age_entry = Entry(main_frame, textvariable=age_value, bg="White", fg="Black")
gender_entry = Entry(main_frame, textvariable=gender_value, bg="White", fg="Black")
phone_entry = Entry(main_frame, textvariable=phone_value, bg="White", fg="Black")
payment_mode_entry = Entry(main_frame, textvariable=payment_mode_value, bg="White", fg="Black")

name_entry.grid(row=0, column=1, padx=(20, 5), pady=(20, 5))
age_entry.grid(row=1, column=1, padx=(20, 5), pady=5)
gender_entry.grid(row=2, column=1, padx=(20, 5), pady=5)
phone_entry.grid(row=3, column=1, padx=(20, 5), pady=5)
payment_mode_entry.grid(row=4, column=1, padx=(20, 5), pady=5)

# Checkbox 
food_service = Checkbutton(main_frame, text="Want to prebook your meals?", variable=food_service_value, bg="PaleTurquoise1",  fg="SlateBlue4", font="helvetica 9 bold") 
food_service.grid(row=5, column=0, columnspan=2, pady=(10, 0))

def submit():
    name = name_value.get()
    age = age_value.get()
    gender = gender_value.get()
    phone = phone_value.get()
    payment_mode = payment_mode_value.get()
    food_service = "Yes" if food_service_value.get() == 1 else "No"
    
    if not name or not age or not gender or not phone or not payment_mode:
        messagebox.showwarning("Warning", "Please fill all the details.")
    else:
        f.add_details(name, age, gender, phone, payment_mode, food_service)
        messagebox.showinfo("Success", "Data stored successfully")
    
        name_value.set("")
        age_value.set("")
        gender_value.set("")
        phone_value.set("")
        payment_mode_value.set("")
        food_service_value.set(0)
    
# Submit button 
Button(main_frame, text="Submit", command=submit, bg="LightGreen", font="helvetica 9 bold", fg="Black", padx=7, pady=3).grid(row=6, column=0, pady=10, columnspan=2)

root.mainloop()
