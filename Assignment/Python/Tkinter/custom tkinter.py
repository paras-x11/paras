import customtkinter as ctk

def submit_form():
    # Retrieve the data entered in the form
    name = entry_name.get()
    email = entry_email.get()
    
    # Print the entered data to the console
    print(f"\nForm Submitted!")
    print(f"Name: {name}")
    print(f"Email: {email}")

# Create the main window
root = ctk.CTk()

# Set the window title and size
root.title("Elegant CTkinter Form")
root.geometry("450x350")

# Add a gradient background (create a smooth color transition)
root.configure(bg="#DCE0E0")

# Create a frame to hold the form elements with rounded corners and shadow effects
form_frame = ctk.CTkFrame(root, width=380, height=250, fg_color="white", corner_radius=15, border_width=2, border_color="#A2A2A2")
form_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame in the window

# Create and place the labels and entry widgets inside the frame
label_name = ctk.CTkLabel(form_frame, text="Full Name:", font=("Helvetica", 14, "bold"), text_color="#333333")
label_name.grid(row=0, column=0, padx=25, pady=15, sticky="e")

entry_name = ctk.CTkEntry(form_frame, font=("Helvetica", 14), width=250, border_width=2, corner_radius=10, placeholder_text="Enter your name")
entry_name.grid(row=0, column=1, padx=25, pady=15)

label_email = ctk.CTkLabel(form_frame, text="Email Address:", font=("Helvetica", 14, "bold"), text_color="#333333")
label_email.grid(row=1, column=0, padx=25, pady=15, sticky="e")

entry_email = ctk.CTkEntry(form_frame, font=("Helvetica", 14), width=250, border_width=2, corner_radius=10, placeholder_text="Enter your email")
entry_email.grid(row=1, column=1, padx=25, pady=15)

# Create a stylish submit button with a gradient color
submit_button = ctk.CTkButton(
    form_frame,
    text="Submit",
    command=submit_form,
    font=("Helvetica", 14, "bold"),
    fg_color="#FF6F61",  # Elegant coral color
    hover_color="#FF4E3A",  # Darker coral on hover
    width=250,
    corner_radius=10,
    border_width=0
)
submit_button.grid(row=2, columnspan=2, pady=25)

# Optional: Add a label for feedback (if desired, like success message)
feedback_label = ctk.CTkLabel(form_frame, text="", font=("Helvetica", 12), text_color="green")
feedback_label.grid(row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()
