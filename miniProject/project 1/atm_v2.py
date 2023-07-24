import tkinter as tk
from tkinter import messagebox
import time

def check_balance():
    messagebox.showinfo("Balance", f"Your Current Balance is ₹{balance:.2f}")

def withdraw_money():
    global balance
    amount = float(withdraw_entry.get())
    if amount > balance:
        messagebox.showerror("Error", "Insufficient balance.")
    else:
        balance -= amount
        messagebox.showinfo("Withdrawal", f"Withdrawn ₹{amount:.2f}. Your remaining balance is ₹{balance:.2f}.")
        update_balance()

def deposit_money():
    global balance
    amount = float(deposit_entry.get())
    balance += amount
    messagebox.showinfo("Deposit", f"Deposited ₹{amount:.2f}. Your new balance is ₹{balance:.2f}.")
    update_balance()

def update_balance():
    balance_label.config(text=f"Balance: ₹{balance:.2f}")

def exit_program():
    global root
    root.destroy()
    messagebox.showinfo("Exit", "Thanks for choosing our ATM!")
def show_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, show_time)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

balance = 10000

root = tk.Tk()
root.title("ATM MACHINE BY MSCETI")
root.geometry("500x550")
root.resizable(False, False)  # Disable horizontal and vertical resizing

# Splash Screen
splash_label = tk.Label(root, text="ATM MACHINE BY MSCETI", font=("Helvetica", 16))
splash_label.pack(pady=50)

# Balance Label
balance_label = tk.Label(root, text=f"Balance: ₹{balance:.2f}", font=("Helvetica",12))
balance_label.pack(pady=10)

# Withdraw Section
withdraw_label = tk.Label(root, text="Withdraw Amount (₹):")
withdraw_label.pack()
withdraw_entry = tk.Entry(root)
withdraw_entry.pack()
withdraw_button = tk.Button(root, text="Withdraw", command=withdraw_money)
withdraw_button.pack(pady=5)

# Deposit Section
deposit_label = tk.Label(root, text="Deposit Amount (₹):")
deposit_label.pack()
deposit_entry = tk.Entry(root)
deposit_entry.pack()
deposit_button = tk.Button(root, text="Deposit", command=deposit_money)
deposit_button.pack(pady=5)

# Check Balance Button
check_balance_button = tk.Button(root, text="Check Balance", command=check_balance)
check_balance_button.pack(pady=20)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()

# Time Label (Top Right Corner)
time_label = tk.Label(root, font=("Helvetica", 10))
time_label.pack(anchor="ne", padx=10, pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)
show_time() 
 # Start showing the current time
root.mainloop()
