import tkinter as tk
from tkinter import messagebox
import string
import secrets

frame = tk.Tk()
frame.title("Random Password Generator")
frame.config(background="grey")
frame.geometry("400x400")

length=tk.Label(frame, text="Enter Length of Password",bg="teal",foreground="yellow", font=("Times New Roman", 15))
length.pack()
length.place(x=20, y=28)

length_entry= tk.Entry(frame, font=("Times New Roman",15))
length_entry.pack()
length_entry.place(x=250, y=28, width=80)

level=tk.Label(frame, text="Choose Difficulty Level of Password", bg="teal", foreground="yellow" , font=("Times New Roman", 15))
level.pack()
level.place(x=20, y=70)

difficulty_var = tk.IntVar()
easy_radio = tk.Radiobutton(frame, text="Easy", variable=difficulty_var, value=0)
easy_radio.place(x=125, y=120)

medium_radio = tk.Radiobutton(frame, text="Medium", variable=difficulty_var, value=1)
medium_radio.place(x=125, y=160)

hard_radio = tk.Radiobutton(frame, text="Hard", variable=difficulty_var, value=2)
hard_radio.place(x=125, y=200)

difficulty_var.set(None)

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length < 8:
        messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
        return

    password_characters = ""
    if difficulty_var.get() == 0:  
        password_characters = string.ascii_letters
    elif difficulty_var.get() == 1:  
        password_characters = string.ascii_letters + string.digits
    elif difficulty_var.get() == 2:  
        password_characters = string.ascii_letters + string.digits + string.punctuation 
    
    password = ''.join(secrets.choice(password_characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.place(x=120, y=250)

password_entry = tk.Entry(frame, show="")
password_entry.place(x=120, y=290)




frame.mainloop()