
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password():

    password_length = int(length_entry.get())
    
    if password_length < 8:
        messagebox.showerror("Invalid Length", "Password length should be at least 8 characters.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for i in range(password_length))
    password_var.set(generated_password)

# Create the main application window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")

# # Set background colo
root.configure(bg="grey")

# # # Create a frame to hold the widgets
frame = tk.Frame(root, bg=" blue",border=10,height=15,  borderwidth=10, )
frame.pack(pady=200)




# Create widgets
length_label = tk.Label(frame, text="Password Length:",font=20, bg="grey",fg="white")
length_label.pack(pady=10,padx=10)

length_entry = tk.Entry(frame, width=60,font=20)
length_entry.pack(pady=10,padx=10)

generate_button = tk.Button(frame, text="Generate Password",font=20, command=generate_password, bg="#FF5733", fg="white",border=1)
generate_button.pack(pady=10,padx=10)

password_var = tk.StringVar()
password_label = tk.Label(frame, text="Generated Password:",font=20, bg="grey",fg="white")
password_label.pack(pady=10,padx=10)

password_entry = tk.Entry(frame, textvariable=password_var, width=50, state="readonly",font=30)
password_entry.pack(pady=1)
root.mainloop()


