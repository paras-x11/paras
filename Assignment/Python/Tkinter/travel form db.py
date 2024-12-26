from tkinter import *
from tkinter import messagebox
import mysql.connector

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

# Center the content within the main frame
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.columnconfigure(0, weight=1)

# Form content frame (for centering)
form_frame = Frame(main_frame, bg="lightskyblue1")
form_frame.grid(row=0, column=0, sticky="")

# Database connection
db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1",
    database="practice"
)
query = db_conn.cursor()

# Function to get the next ID
def get_next_id():
    query.execute("SELECT COUNT(*) FROM travel_form")
    count = query.fetchone()[0]  # Fetch the number of rows
    return count + 1

# Create the ID label and disabled entry
id_value = StringVar()
id_value.set(get_next_id())

id_label = Label(form_frame, text="ID: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
id_entry = Entry(form_frame, textvariable=id_value, state="disabled", bg="LightGray", fg="Black")

id_label.grid(row=0, column=0, sticky=W, padx=(20, 5), pady=(20, 5))
id_entry.grid(row=0, column=1, padx=(20, 5), pady=(20, 5))

# Details labels
name = Label(form_frame, text="Name: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
age = Label(form_frame, text="Age: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
gender = Label(form_frame, text="Gender: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
phone = Label(form_frame, text="Phone No: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
payment_mode = Label(form_frame, text="Payment Mode: ", font="helvetica 11 bold", bg="CadetBlue", fg="White") 

name.grid(row=1, column=0, sticky=W, padx=(20, 5), pady=(20, 5))
age.grid(row=2, column=0, sticky=W, padx=(20, 5), pady=5)
gender.grid(row=3, column=0, sticky=W, padx=(20, 5), pady=5)
phone.grid(row=4, column=0, sticky=W, padx=(20, 5), pady=5)
payment_mode.grid(row=5, column=0, sticky=W, padx=(20, 5), pady=5)

# Details variable
name_value = StringVar()
age_value = StringVar()
gender_value = StringVar()
phone_value = StringVar()
payment_mode_value = StringVar()
food_service_value = IntVar()

# Detail entries 
name_entry = Entry(form_frame, textvariable=name_value, bg="White", fg="Black")
age_entry = Entry(form_frame, textvariable=age_value, bg="White", fg="Black")
gender_entry = Entry(form_frame, textvariable=gender_value, bg="White", fg="Black")
phone_entry = Entry(form_frame, textvariable=phone_value, bg="White", fg="Black")
payment_mode_entry = Entry(form_frame, textvariable=payment_mode_value, bg="White", fg="Black")

name_entry.grid(row=1, column=1, padx=(20, 5), pady=(20, 5))
age_entry.grid(row=2, column=1, padx=(20, 5), pady=5)
gender_entry.grid(row=3, column=1, padx=(20, 5), pady=5)
phone_entry.grid(row=4, column=1, padx=(20, 5), pady=5)
payment_mode_entry.grid(row=5, column=1, padx=(20, 5), pady=5)

# Checkbox 
food_service = Checkbutton(form_frame, text="Want to prebook your meals?", variable=food_service_value, bg="PaleTurquoise1",  fg="SlateBlue4", font="helvetica 9 bold") 
food_service.grid(row=6, column=0, columnspan=2, pady=(11, 0))

# Submit function
def submit():
    id_ = id_value.get()
    name = name_value.get()
    age = age_value.get()
    gender = gender_value.get()
    phone = phone_value.get()
    payment_mode = payment_mode_value.get()
    food_service = "Yes" if food_service_value.get() == 1 else "No"

    if not name or not age or not gender or not phone or not payment_mode:
        messagebox.showwarning("Warning", "Please fill all the details.")
    else:
        qry = "INSERT INTO travel_form (name, age, gender, phone_no, payment_mode, food_service) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, age, gender, phone, payment_mode, food_service)

        query.execute(qry, values)
        db_conn.commit()
        messagebox.showinfo("Success", "Data stored successfully")

        # Clear inputs and update next ID
        name_value.set("")
        age_value.set("")
        gender_value.set("")
        phone_value.set("")
        payment_mode_value.set("")
        food_service_value.set(0)
        id_value.set(get_next_id())

# Submit button 
Button(form_frame, text="Submit", command=submit, bg="LightGreen", font="helvetica 11 bold", fg="Black", padx=7, pady=3).grid(row=7, column=0, pady=11, columnspan=2)

root.mainloop()
