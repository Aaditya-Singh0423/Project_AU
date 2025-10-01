import tkinter as tk
from tkinter import ttk, messagebox
import pickle, os
from student import Students

# -----------------------------
# Storage Functions
# -----------------------------
FILENAME = "students.pkl"

def save_Student_data(student):
    """Save a student object into pickle file"""
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
    data.append({"name": student.name, "rollno": student.rollno, "marks": student.marks})
    with open(FILENAME, "wb") as f:
        pickle.dump(data, f)

def load_data():
    """Load student records from pickle file"""
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            try:
                return pickle.load(f)
            except EOFError:
                return []
    return []

# -----------------------------
# GUI Class
# -----------------------------
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f8ff")

        # Title
        title = tk.Label(
            root,
            text="🎓 Student Management System",
            font=("Arial", 20, "bold"),
            bg="#4682b4",
            fg="white",
            pady=15
        )
        title.pack(fill="x")

        # Buttons Frame
        button_frame = tk.Frame(root, bg="#f0f8ff")
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="➕ Add Student", width=20, command=self.add_student).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(button_frame, text="📋 Display Students", width=20, command=self.display_students).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(button_frame, text="❌ Exit", width=20, command=root.quit).grid(row=0, column=2, padx=10, pady=10)

    def add_student(self):
        """Window to add a new student"""
        win = tk.Toplevel(self.root)
        win.title("Add Student")
        win.geometry("400x300")

        tk.Label(win, text="Enter Student Name:").pack(pady=5)
        name_entry = ttk.Entry(win, width=30)
        name_entry.pack(pady=5)

        tk.Label(win, text="Enter Roll Number:").pack(pady=5)
        roll_entry = ttk.Entry(win, width=30)
        roll_entry.pack(pady=5)

        tk.Label(win, text="Enter Marks:").pack(pady=5)
        marks_entry = ttk.Entry(win, width=30)
        marks_entry.pack(pady=5)

        def save_student():
            try:
                name = name_entry.get().strip()
                rollno = int(roll_entry.get())
                marks = int(marks_entry.get())

                if not name:
                    messagebox.showerror("Error", "Name cannot be empty")
                    return

                s = Students(name, rollno, marks)
                save_Student_data(s)  # ✅ Connected to pickle
                messagebox.showinfo("Success", "Student data saved successfully!")
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Roll No and Marks must be numbers")

        ttk.Button(win, text="Save", command=save_student).pack(pady=20)

    def display_students(self):
        """Window to display all students"""
        win = tk.Toplevel(self.root)
        win.title("Student Records")
        win.geometry("600x400")

        columns = ("Name", "Roll No", "Marks")
        tree = ttk.Treeview(win, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        tree.pack(fill="both", expand=True)

        # Fetch data from pickle
        students = load_data()
        if students:
            for stu in students:
                tree.insert("", tk.END, values=(stu["name"], stu["rollno"], stu["marks"]))
        else:
            messagebox.showinfo("Info", "No student records found.")


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
