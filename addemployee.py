import tkinter as tk
from tkinter import messagebox
import sqlite3

class AddEmployeeApp:
    def __init__(self, root, go_back_home):
        self.root = root
        self.root.title("Add Employee")
        self.root.configure(bg="#1D5B79")


        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - 400) // 2
        y_coordinate = (screen_height - 300) // 2
        self.root.geometry(f"1500x700+{x_coordinate}+{y_coordinate}")


        self.border_frame = tk.Frame(root, pady=60, padx=60, bd=5, relief=tk.GROOVE, bg="#468B97")
        self.border_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.go_back_home = go_back_home


        self.add_employee_label = tk.Label(self.border_frame, text="Add Employee", font=("Helvetica", 16, "bold"), bg="#468B97", fg="white")
        self.add_employee_label.grid(row=0, column=0, columnspan=2, pady=10)


        self.create_database()

        self.employee_id_label = tk.Label(self.border_frame, text="Employee ID:", bg="#468B97", fg="white")
        self.employee_id_label.grid(row=1, column=0, pady=5, padx=5)
        self.employee_id_entry = tk.Entry(self.border_frame)
        self.employee_id_entry.grid(row=1, column=1, pady=5, padx=5)

        self.name_label = tk.Label(self.border_frame, text="Name:", bg="#468B97", fg="white")
        self.name_label.grid(row=2, column=0, pady=5, padx=5)
        self.name_entry = tk.Entry(self.border_frame)
        self.name_entry.grid(row=2, column=1, pady=5, padx=5)

        self.position_label = tk.Label(self.border_frame, text="Position:", bg="#468B97", fg="white" )
        self.position_label.grid(row=3, column=0, pady=5, padx=5)
        self.position_entry = tk.Entry(self.border_frame)
        self.position_entry.grid(row=3, column=1, pady=5, padx=5)

        self.salary_label = tk.Label(self.border_frame, text="Salary:", bg="#468B97", fg="white")
        self.salary_label.grid(row=4, column=0, pady=5, padx=5)
        self.salary_entry = tk.Entry(self.border_frame)
        self.salary_entry.grid(row=4, column=1, pady=5, padx=5)

        self.add_button = tk.Button(self.border_frame, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.back_button = tk.Button(self.border_frame, text="Back", command=self.go_back)
        self.back_button.grid(row=6, column=0, columnspan=2, pady=10)

    def create_database(self):

        conn = sqlite3.connect("employee_database.db")
        cursor = conn.cursor()


        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER,
                name TEXT,
                position TEXT,
                salary REAL
            )
        ''')


        conn.commit()
        conn.close()

    def add_employee(self):
        name = self.name_entry.get().strip()
        salary = self.salary_entry.get().strip()
        position = self.position_entry.get().strip()
        employee_id = self.employee_id_entry.get().strip()

        if not name or not salary or not position or not employee_id:
            messagebox.showerror("Error", "Please enter name, salary, position, and employee ID")
            return

        try:
            salary = float(salary)
            employee_id = int(employee_id)


            conn = sqlite3.connect("employee_database.db")
            cursor = conn.cursor()


            cursor.execute("INSERT INTO employees (employee_id, name, position, salary) VALUES (?, ?, ?, ?)",
                           (employee_id, name, position, salary))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Employee added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid salary or employee ID. Please enter valid numbers.")

    def go_back(self):
        self.root.destroy()
        self.go_back_home()

if __name__ == "__main__":
    root = tk.Tk()
    add_employee_app = AddEmployeeApp(root, root.quit)
    root.mainloop()
