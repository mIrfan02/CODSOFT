import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def update_contact(self, name, phone, email, address):
        contact = self.find_contact(name)
        if contact:
            contact.phone = phone
            contact.email = email
            contact.address = address
            return True
        return False

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

def add_contact_window():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact_manager.add_contact(name, phone, email, address)
        clear_fields()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and phone fields are required.")

def update_contact_window():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        if contact_manager.update_contact(name, phone, email, address):
            clear_fields()
            update_contact_list()
        else:
            messagebox.showerror("Error", "Contact not found.")
    else:
        messagebox.showerror("Error", "Name and phone fields are required.")

def delete_contact_window():
    name = name_entry.get()

    if name:
        if contact_manager.delete_contact(name):
            clear_fields()
            update_contact_list()
        else:
            messagebox.showerror("Error", "Contact not found.")
    else:
        messagebox.showerror("Error", "Name field is required.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contact_manager.contacts:
        contact_list.insert(tk.END, contact.name)

def view_contact_window():
    name = contact_list.get(contact_list.curselection())
    contact = contact_manager.find_contact(name)
    if contact:
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        name_entry.insert(0, contact.name)
        phone_entry.insert(0, contact.phone)
        email_entry.insert(0, contact.email)
        address_entry.insert(0, contact.address)

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def main():
    global name_entry, phone_entry, email_entry, address_entry, contact_list, contact_manager

    contact_manager = ContactManager()

    app = tk.Tk()
    app.title("Contact Manager")

    tk.Label(app, text="Name:").grid(row=0, column=0)
    tk.Label(app, text="Phone:").grid(row=1, column=0)
    tk.Label(app, text="Email:").grid(row=2, column=0)
    tk.Label(app, text="Address:").grid(row=3, column=0)

    name_entry = tk.Entry(app)
    phone_entry = tk.Entry(app)
    email_entry = tk.Entry(app)
    address_entry = tk.Entry(app)

    name_entry.grid(row=0, column=1)
    phone_entry.grid(row=1, column=1)
    email_entry.grid(row=2, column=1)
    address_entry.grid(row=3, column=1)

    add_button = tk.Button(app, text="Add Contact", command=add_contact_window)
    update_button = tk.Button(app, text="Update Contact", command=update_contact_window)
    delete_button = tk.Button(app, text="Delete Contact", command=delete_contact_window)

    add_button.grid(row=4, column=0)
    update_button.grid(row=4, column=1)
    delete_button.grid(row=4, column=2)

    contact_list = tk.Listbox(app, selectmode=tk.SINGLE)
    contact_list.grid(row=5, column=0, columnspan=3)
    update_contact_list()

    view_button = tk.Button(app, text="View Contact", command=view_contact_window)
    view_button.grid(row=6, column=0, columnspan=3)

    app.mainloop()

if __name__ == "__main__":
    main()
