import tkinter as tk
import random

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_choice_label.config(text=user_choice)
    computer_choice_label.config(text=computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"
        result_label.config(fg="orange")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        result_label.config(fg="green")
    else:
        result = "Computer Wins!"
        result_label.config(fg="crimson")

    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Title
title = tk.Label(root, text="Rock - Paper - Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=12, font=("Arial", 14), bg="#d6e0f0", command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Paper", width=12, font=("Arial", 14), bg="#f9d6d5", command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Scissors", width=12, font=("Arial", 14), bg="#e4f9d6", command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Opponent view layout
battle_frame = tk.Frame(root, bg="#f0f0f0")
battle_frame.pack(pady=30)

user_label = tk.Label(battle_frame, text="You", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0")
user_label.grid(row=0, column=0, padx=60)

vs_label = tk.Label(battle_frame, text="VS", font=("Arial", 14, "bold"), bg="#f0f0f0")
vs_label.grid(row=0, column=1, padx=10)

comp_label = tk.Label(battle_frame, text="Computer", font=("Arial", 14, "bold"), fg="red", bg="#f0f0f0")
comp_label.grid(row=0, column=2, padx=60)

user_choice_label = tk.Label(battle_frame, text="", font=("Arial", 16), bg="#d6e0f0", width=12, relief="ridge")
user_choice_label.grid(row=1, column=0, pady=10)

blank = tk.Label(battle_frame, text="", bg="#f0f0f0")
blank.grid(row=1, column=1)

computer_choice_label = tk.Label(battle_frame, text="", font=("Arial", 16), bg="#f9d6d5", width=12, relief="ridge")
computer_choice_label.grid(row=1, column=2)

# Result
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f0f0f0")
result_label.pack(pady=20)

root.mainloop()
