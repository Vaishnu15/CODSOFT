import tkinter as tk
from tkinter import messagebox, Toplevel

def open_calculator():
    calc_win = Toplevel(root)
    calc_win.title("Formula Calculator")
    calc_win.geometry("500x400")
    calc_win.configure(bg="#e6f2ff")

    # Labels and Entry widgets
    tk.Label(calc_win, text="Enter First Number:", font=("Arial", 14), bg="#e6f2ff").pack(pady=10)
    num1_entry = tk.Entry(calc_win, font=("Arial", 14))
    num1_entry.pack()

    tk.Label(calc_win, text="Enter Second Number:", font=("Arial", 14), bg="#e6f2ff").pack(pady=10)
    num2_entry = tk.Entry(calc_win, font=("Arial", 14))
    num2_entry.pack()

    tk.Label(calc_win, text="Operation (+, -, *, /, **, sqrt, %):", font=("Arial", 14), bg="#e6f2ff").pack(pady=10)
    op_entry = tk.Entry(calc_win, font=("Arial", 14))
    op_entry.pack()

    result_label = tk.Label(calc_win, text="", font=("Arial", 16, "bold"), bg="#e6f2ff", fg="green")
    result_label.pack(pady=20)

    def perform_calculation():
        try:
            a = float(num1_entry.get())
            b = float(num2_entry.get())
            op = op_entry.get().strip()

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b
            elif op == '**':
                result = a ** b
            elif op == '%':
                result = a % b
            elif op == 'sqrt':
                from math import sqrt
                result = f"sqrt({a}) = {sqrt(a)}, sqrt({b}) = {sqrt(b)}"
            else:
                result = "Invalid operation"

            result_label.config(text=f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong.\n{e}")

    tk.Button(calc_win, text="Calculate", command=perform_calculation, font=("Arial", 13), bg="#cce6ff").pack(pady=10)

# Main window to launch task
root = tk.Tk()
root.title("Task 2 - Formula Calculator")
root.geometry("400x200")
root.configure(bg="#f0f8ff")

tk.Label(root, text="Click to open Formula Calculator", font=("Arial", 14), bg="#f0f8ff").pack(pady=30)
tk.Button(root, text="Open Calculator", command=open_calculator, font=("Arial", 12), bg="#d1e0e0").pack()

root.mainloop()
