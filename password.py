import tkinter as tk
import random
import string
from tkinter import messagebox, Toplevel

def open_password_generator():
    gen_win = Toplevel(root)
    gen_win.title("Password Generator")
    gen_win.geometry("500x400")
    gen_win.configure(bg="#fff0f5")

    # --- UI Elements ---
    tk.Label(gen_win, text="Enter Username:", font=("Arial", 14), bg="#fff0f5").pack(pady=10)
    username_entry = tk.Entry(gen_win, font=("Arial", 14))
    username_entry.pack()

    tk.Label(gen_win, text="Enter Password Length:", font=("Arial", 14), bg="#fff0f5").pack(pady=10)
    length_entry = tk.Entry(gen_win, font=("Arial", 14))
    length_entry.pack()

    symbol_var = tk.BooleanVar()
    tk.Checkbutton(gen_win, text="Include Symbols", variable=symbol_var, font=("Arial", 12), bg="#fff0f5").pack(pady=10)

    result_label = tk.Label(gen_win, text="", font=("Arial", 16, "bold"), bg="#fff0f5", fg="blue")
    result_label.pack(pady=20)

    def generate_password():
        username = username_entry.get()
        try:
            length = int(length_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")
            return

        if not username:
            messagebox.showwarning("Missing Username", "Please enter a username.")
            return

        if length < 6:
            messagebox.showwarning("Length Too Short", "Password length should be at least 6.")
            return

        chars = string.ascii_letters + string.digits
        if symbol_var.get():
            chars += string.punctuation

        random.seed(username)  # Makes it unique to username
        password = ''.join(random.choices(chars, k=length))

        result_label.config(text=f"Generated Password: {password}")

    tk.Button(gen_win, text="Generate Password", command=generate_password, font=("Arial", 13), bg="#ffe6f0").pack(pady=10)

# --- Main Launcher Window ---
root = tk.Tk()
root.title("Task 3 - Password Generator")
root.geometry("400x200")
root.configure(bg="#f9f9f9")

tk.Label(root, text="Click to open Password Generator", font=("Arial", 14), bg="#f9f9f9").pack(pady=30)
tk.Button(root, text="Open Generator", command=open_password_generator, font=("Arial", 12), bg="#d1e0e0").pack()

root.mainloop()
