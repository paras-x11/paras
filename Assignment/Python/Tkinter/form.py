from tkinter import *
from tkinter import messagebox

class File_Handler():
    
    def add_details(self, details):
        with open("Form_data.txt", 'a') as f:
            f.write(f"{details}")
    
    def read_details(self):
        with open("Form_data.txt", 'r') as f:
            data = f.read()
            if not data:
                print("-> Empty. ")
            else:
                print(data)

f = File_Handler()

total_persons = 1

def store_details():
    global total_persons 
    
    name = name_var.get()
    dob= dob_var.get()
    gender= gender_var.get()
    email =email_var.get()
    phone = phone_var.get()

    if not name or not dob or not gender or not email or not phone:
        messagebox.showwarning("Warning", "Enter all the details.")
    
    else:
        data = {'Name' : name, 'DOB':dob, 'Gender':gender, 'E-mail':email, 'Phone no':phone}
        print(data)
        
        f.add_details(f"-> Person {total_persons}- \n")
        for key, val in data.items():
            f.add_details(f"{key}: {val}\n")   
        f.add_details("\n")
            
        messagebox.showinfo("Success", "Form submitted successfully!")
        
        name_var.set("")
        dob_var.set("")
        gender_var.set("")
        email_var.set("")
        phone_var.set("")
        
        total_persons = total_persons + 1
    
    
root = Tk()
root.title("Registration Form")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.geometry("727x427")

name_var = StringVar()
dob_var = StringVar()
gender_var = StringVar()
email_var = StringVar()
phone_var = StringVar()

# Background frame with a subtle light blue and a soft shadowed border
bg_frame = Frame(root, bg="LightSkyBlue1", borderwidth=10, relief=GROOVE)  # Light sky blue
bg_frame.grid(row=0, column=0, sticky=NSEW, padx=20, pady=20)

# Labels with a muted dark gray for elegance
name = Label(bg_frame, text="Name: ", font="helvetica 10 bold", bg="LightSkyBlue1", fg="black")  
name.grid(row=0, column=0, sticky=W, padx=(25, 5), pady=(15, 5))
name_val = Entry(bg_frame, textvariable=name_var, bg="white", fg="black", bd=2, relief=SOLID) 
name_val.grid(row=0, column=1, pady=(15, 5))

dob = Label(bg_frame, text="DOB: ", font="helvetica 10 bold", bg="LightSkyBlue1", fg="black")
dob.grid(row=1, column=0, sticky=W, padx=(25, 5), pady=5)
dob_val = Entry(bg_frame, textvariable=dob_var, bg="white", fg="black", bd=2, relief=SOLID)
dob_val.grid(row=1, column=1)

gender = Label(bg_frame, text="Gender: ", font="helvetica 10 bold", bg="LightSkyBlue1", fg="black")
gender.grid(row=2, column=0, sticky=W, padx=(25, 5), pady=5)
gender_val = Entry(bg_frame, textvariable=gender_var, bg="white", fg="black", bd=2, relief=SOLID)
gender_val.grid(row=2, column=1)

email = Label(bg_frame, text="E-mail: ", font="helvetica 10 bold", bg="LightSkyBlue1", fg="black")
email.grid(row=3, column=0, sticky=W, padx=(25, 5), pady=5)
email_val = Entry(bg_frame, textvariable=email_var, bg="white", fg="black", bd=2, relief=SOLID)
email_val.grid(row=3, column=1)

phone = Label(bg_frame, text="Phone No: ", font="helvetica 10 bold", bg="LightSkyBlue1", fg="black")
phone.grid(row=4, column=0, sticky=W, padx=(25, 5), pady=5)
phone_val = Entry(bg_frame, textvariable=phone_var, bg="white", fg="black", bd=2, relief=SOLID)
phone_val.grid(row=4, column=1)

btn = Button(bg_frame, text="Submit", borderwidth=5, relief=RAISED, font="helvetica 10 bold", bg="MediumSeaGreen", fg="black", padx=10)  
btn.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

btn.config(command=store_details)

root.mainloop()
