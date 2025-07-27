import tkinter as tk
from tkinter import messagebox

contacts = {}

# --- Functions ---
def create_contact():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if name in contacts:
        messagebox.showwarning("Duplicate", f"Contact '{name}' already exists.")
    elif not (name and age and email and phone):
        messagebox.showerror("Input Error", "All fields are required!")
    else:
        contacts[name] = {"age": age, "email": email, "phone": phone}
        update_display()
        messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
        clear_entries()

def view_contact():
    name = name_entry.get()
    if name in contacts:
        info = contacts[name]
        result = f"Name: {name}\nAge: {info['age']}\nEmail: {info['email']}\nPhone: {info['phone']}"
        messagebox.showinfo("Contact Details", result)
    else:
        messagebox.showerror("Not Found", "Contact not found.")

def update_contact():
    name = name_entry.get()
    if name in contacts:
        contacts[name] = {
            "age": age_entry.get(),
            "email": email_entry.get(),
            "phone": phone_entry.get()
        }
        update_display()
        messagebox.showinfo("Updated", f"Contact '{name}' updated.")
        clear_entries()
    else:
        messagebox.showerror("Not Found", "Contact not found.")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        update_display()
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
        clear_entries()
    else:
        messagebox.showerror("Not Found", "Contact not found.")

def search_contact():
    query = name_entry.get().lower()
    found = False
    result = ""
    for name, info in contacts.items():
        if query in name.lower():
            result += f"{name}: {info}\n"
            found = True
    if found:
        messagebox.showinfo("Search Results", result)
    else:
        messagebox.showinfo("Not Found", "No matching contacts.")

def count_contacts():
    count = len(contacts)
    messagebox.showinfo("Total Contacts", f"You have {count} contact(s).")

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def update_display():
    display.delete(1.0, tk.END)
    for name, info in contacts.items():
        display.insert(tk.END, f"{name}: Age={info['age']}, Email={info['email']}, Phone={info['phone']}\n")

# --- GUI Setup ---
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x500")
root.config(bg="#f0f8ff")

title = tk.Label(root, text="Contact Book App", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="blue")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack()

# Input Fields
tk.Label(frame, text="Name:", bg="#f0f8ff").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Age:", bg="#f0f8ff").grid(row=1, column=0, sticky="e")
age_entry = tk.Entry(frame, width=30)
age_entry.grid(row=1, column=1)

tk.Label(frame, text="Email:", bg="#f0f8ff").grid(row=2, column=0, sticky="e")
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1)

tk.Label(frame, text="Phone:", bg="#f0f8ff").grid(row=3, column=0, sticky="e")
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=3, column=1)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Create", width=10, command=create_contact, bg="green", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View", width=10, command=view_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_contact, bg="orange").grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_contact, bg="red", fg="white").grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Search", width=10, command=search_contact).grid(row=1, column=0, pady=5)
tk.Button(btn_frame, text="Count", width=10, command=count_contacts).grid(row=1, column=1, pady=5)
tk.Button(btn_frame, text="Clear", width=10, command=clear_entries).grid(row=1, column=2, pady=5)
tk.Button(btn_frame, text="Exit", width=10, command=root.quit, bg="black", fg="white").grid(row=1, column=3, pady=5)

# Display Box
display = tk.Text(root, height=10, width=70)
display.pack(pady=10)

# Run the GUI loop
root.mainloop()
