import tkinter as tk
from tkinter import ttk, messagebox

class BankATM:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank ATM")
        self.root.geometry("500x500")
        self.root.configure(bg="#e6f0ff")

        # ATM properties
        self.bal = 0.0
        self.pin = ""

        # Title
        title = tk.Label(root, text="🏦 Welcome to Bank ATM", font=("Arial", 20, "bold"), bg="#007acc", fg="white", pady=15)
        title.pack(fill="x")

        # Balance Label (updates dynamically)
        self.balance_label = tk.Label(root, text=f"💰 Balance: ₹{self.bal}", font=("Arial", 14), bg="#e6f0ff", fg="black")
        self.balance_label.pack(pady=15)

        # Buttons frame
        button_frame = tk.Frame(root, bg="#e6f0ff")
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="Set Balance", width=25, command=self.set_balance).grid(row=0, column=0, pady=8)
        ttk.Button(button_frame, text="Set PIN", width=25, command=self.set_pin).grid(row=1, column=0, pady=8)
        ttk.Button(button_frame, text="Check Balance", width=25, command=self.check_balance).grid(row=2, column=0, pady=8)
        ttk.Button(button_frame, text="Withdraw", width=25, command=self.withdraw).grid(row=3, column=0, pady=8)
        ttk.Button(button_frame, text="Exit", width=25, command=root.quit).grid(row=4, column=0, pady=8)

    def update_balance_label(self):
        """Update the balance display"""
        self.balance_label.config(text=f"💰 Balance: ₹{self.bal}")

    def set_balance(self):
        def save_balance():
            try:
                amount = float(entry.get())
                self.bal = amount
                self.update_balance_label()
                messagebox.showinfo("Success", f"Balance set to ₹{self.bal}")
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number")

        win = tk.Toplevel(self.root)
        win.title("Set Balance")
        win.geometry("300x150")
        ttk.Label(win, text="Enter Amount:").pack(pady=10)
        entry = ttk.Entry(win)
        entry.pack(pady=5)
        ttk.Button(win, text="Save", command=save_balance).pack(pady=10)

    def set_pin(self):
        def save_pin():
            if entry.get().isdigit() and len(entry.get()) == 4:  # 4-digit PIN
                self.pin = entry.get()
                messagebox.showinfo("Success", "PIN set successfully!")
                win.destroy()
            else:
                messagebox.showerror("Error", "PIN must be a 4-digit number")

        win = tk.Toplevel(self.root)
        win.title("Set PIN")
        win.geometry("300x150")
        ttk.Label(win, text="Enter New 4-digit PIN:").pack(pady=10)
        entry = ttk.Entry(win, show="*")
        entry.pack(pady=5)
        ttk.Button(win, text="Save", command=save_pin).pack(pady=10)

    def check_balance(self):
        def process_check():
            if pin_entry.get() == self.pin:
                messagebox.showinfo("Balance", f"Your current balance is ₹{self.bal}")
                win.destroy()
            else:
                messagebox.showerror("Error", "Incorrect PIN")

        win = tk.Toplevel(self.root)
        win.title("Check Balance")
        win.geometry("300x150")
        ttk.Label(win, text="Enter PIN:").pack(pady=10)
        pin_entry = ttk.Entry(win, show="*")
        pin_entry.pack(pady=5)
        ttk.Button(win, text="Check", command=process_check).pack(pady=10)

    def withdraw(self):
        def process_withdraw():
            pin_entered = pin_entry.get()
            if pin_entered != self.pin:
                messagebox.showerror("Error", "Incorrect PIN")
                return

            try:
                amount = float(amount_entry.get())
                if amount <= self.bal:
                    self.bal -= amount
                    self.update_balance_label()
                    messagebox.showinfo("Success", f"Withdrawn ₹{amount}\nRemaining Balance: ₹{self.bal}")
                    win.destroy()
                else:
                    messagebox.showerror("Error", "Insufficient Balance")
            except ValueError:
                messagebox.showerror("Error", "Enter a valid amount")

        win = tk.Toplevel(self.root)
        win.title("Withdraw Money")
        win.geometry("300x200")
        ttk.Label(win, text="Enter PIN:").pack(pady=5)
        pin_entry = ttk.Entry(win, show="*")
        pin_entry.pack(pady=5)
        ttk.Label(win, text="Enter Amount:").pack(pady=5)
        amount_entry = ttk.Entry(win)
        amount_entry.pack(pady=5)
        ttk.Button(win, text="Withdraw", command=process_withdraw).pack(pady=10)


# Run ATM GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BankATM(root)
    root.mainloop()
