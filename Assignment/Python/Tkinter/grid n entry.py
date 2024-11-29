from tkinter import *
from tkinter import messagebox

def submit_form():
    name = name_val.get()
    dob = dob_val.get()
    gender = gender_val.get()
    phone = phone_val.get()
    email = email_val.get()
    
    if not name or not dob or not gender or not phone or not email:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    messagebox.showinfo("Success", "Form submitted successfully!")

    print(f"Name: {name}")
    print(f"Date of Birth: {dob}")
    print(f"Gender: {gender}")
    print(f"Phone No.: {phone}")
    print(f"E-mail: {email}")

root = Tk()
root.title("Registration Form")
root.geometry("727x527")

# Configuring grid for better responsiveness
root.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand


bg_frame = Frame(root, bg="light blue", borderwidth=10, relief=SUNKEN)
bg_frame.grid(row=0, column=0, sticky=NSEW, padx=20, pady=20)  


name_label = Label(bg_frame, text="Full Name: ", font=("Helvetica", 10), bg="white", padx=10)
name_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
name_val = Entry(bg_frame, width=30)
name_val.grid(row=0, column=1, padx=10, pady=10)


dob_label = Label(bg_frame, text="Date of Birth (DD/MM/YYYY): ", font=("Helvetica", 10), bg="white", padx=10)
dob_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
dob_val = Entry(bg_frame, width=30)
dob_val.grid(row=1, column=1, padx=10, pady=10)


gender_label = Label(bg_frame, text="Gender: ", font=("Helvetica", 10), bg="white", padx=10)
gender_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
gender_val = Entry(bg_frame, width=30)
gender_val.grid(row=2, column=1, padx=10, pady=10)


phone_label = Label(bg_frame, text="Phone Number: ", font=("Helvetica", 10), bg="white", padx=10)
phone_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)
phone_val = Entry(bg_frame, width=30)
phone_val.grid(row=3, column=1, padx=10, pady=10)


email_label = Label(bg_frame, text="E-mail: ", font=("Helvetica", 10), bg="white", padx=10)
email_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)
email_val = Entry(bg_frame, width=30)
email_val.grid(row=4, column=1, padx=10, pady=10)


btn = Button(bg_frame, text="Submit", bg="light green", font="Helvetica 10 bold", fg="red", command=submit_form)
btn.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
