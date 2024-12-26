from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title("My GUI - Student Record System")
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

heading = Label(header_frame, text="Student Record System", font="cosmic 20 bold", bg="Teal", fg="White", padx=5, pady=5)
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
students = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1",
    database="practice"
)
query = students.cursor()

# Function to get the next ID
def get_next_id():
    query.execute("SELECT COUNT(*) FROM student_records")
    count = query.fetchone()[0]  # Fetch the number of rows
    return count + 1

# Create the ID label and disabled entry
id_value = StringVar()
id_value.set(get_next_id())

stud_id = Label(form_frame, text="Student ID: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
stud_id_entry = Entry(form_frame, textvariable=id_value, state="normal", bg="LightGray", fg="Black")

stud_id.grid(row=0, column=0, sticky=W, padx=(20, 5), pady=(20, 5))
stud_id_entry.grid(row=0, column=1, padx=(20, 5), pady=(20, 5))

# Details labels
name = Label(form_frame, text="Name: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
age = Label(form_frame, text="Age: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
city = Label(form_frame, text="City: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
stud_class = Label(form_frame, text="Class: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")
phone = Label(form_frame, text="Phone No: ", font="helvetica 11 bold", bg="CadetBlue", fg="White")

name.grid(row=1, column=0, sticky=W, padx=(20, 5), pady=(20, 5))
age.grid(row=2, column=0, sticky=W, padx=(20, 5), pady=5)
city.grid(row=3, column=0, sticky=W, padx=(20, 5), pady=5)
stud_class.grid(row=4, column=0, sticky=W, padx=(20, 5), pady=5)
phone.grid(row=5, column=0, sticky=W, padx=(20, 5), pady=5)

# Details variable
name_value = StringVar()
age_value = StringVar()
city_value = StringVar()
stud_class_value = StringVar()
phone_value = StringVar()

# Detail entries 
name_entry = Entry(form_frame, textvariable=name_value, bg="White", fg="Black")
age_entry = Entry(form_frame, textvariable=age_value, bg="White", fg="Black")
city_entry = Entry(form_frame, textvariable=city_value, bg="White", fg="Black")
stud_class_entry = Entry(form_frame, textvariable=stud_class_value, bg="White", fg="Black")
phone_entry = Entry(form_frame, textvariable=phone_value, bg="White", fg="Black")

name_entry.grid(row=1, column=1, padx=(20, 5), pady=(20, 5))
age_entry.grid(row=2, column=1, padx=(20, 5), pady=5)
city_entry.grid(row=3, column=1, padx=(20, 5), pady=5)
stud_class_entry.grid(row=4, column=1, padx=(20, 5), pady=5)
phone_entry.grid(row=5, column=1, padx=(20, 5), pady=5)


# Add function
def add():
    id = id_value.get()
    name = name_value.get()
    age = age_value.get()
    city = city_value.get()
    stud_class = stud_class_value.get()
    phone = phone_value.get()

    if not id or not name or not age or not city or not stud_class or not phone:
        messagebox.showwarning("Warning", "Please fill all the details.")
    else:
        qry = "INSERT INTO student_records (id, name, age, city, class, phone_no) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id, name, age, city, stud_class, phone)

        query.execute(qry, values)
        students.commit()
        messagebox.showinfo("Success", "Data stored successfully")
        print("Success", "-> Data stored successfully")

        # Clear inputs and update next ID
        name_value.set("")
        age_value.set("")
        city_value.set("")
        stud_class_value.set("")
        phone_value.set("")
        id_value.set(get_next_id())


button_frame = Frame(main_frame, bg="lightskyblue1")
button_frame.grid(row=1, column=0, pady=(10, 20)) 

# Add button
add_btn = Button(button_frame, text="Add", command=add, bg="LightGreen", font="helvetica 11 bold", fg="Black", padx=20, pady=5)
add_btn.grid(row=0, column=0, padx=15)

# Update function
def update():
    pass  

# Update button
update_btn = Button(button_frame, text="Update", command=update, bg="LightBlue", font="helvetica 11 bold", fg="Black", padx=20, pady=5)
update_btn.grid(row=0, column=1, padx=15)

# Delete function
def delete():
    pass  

# Delete button
delete_btn = Button(button_frame, text="Delete", command=delete, bg="LightCoral", font="helvetica 11 bold", fg="Black", padx=20, pady=5)
delete_btn.grid(row=0, column=2, padx=15)

root.mainloop()
