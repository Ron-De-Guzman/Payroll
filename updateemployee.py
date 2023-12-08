

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class UpdateEmployeeApp:
    def __init__(self, parent, employee_id, refresh_employee_list):
        self.parent = parent
        self.parent.title("Update Employee")
        self.parent.configure(bg="#1D5B79")
        self.parent.geometry("1500x700")

        self.employee_id = employee_id
        self.refresh_employee_list = refresh_employee_list


        self.conn = sqlite3.connect("employee_database.db")
        self.cursor = self.conn.cursor()


        self.cursor.execute("SELECT name, position, salary FROM employees WHERE employee_id=?", (self.employee_id,))
        employee_details = self.cursor.fetchone()


        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background="#468B97")  # Set background color


        self.border_frame = ttk.Frame(parent, style="Custom.TFrame", borderwidth=2, relief="solid")
        self.border_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.name_label = tk.Label(self.border_frame, text="Name:", font=('Helvetica', 12, 'bold'), bg="#468B97", fg="white")
        self.name_entry = tk.Entry(self.border_frame, textvariable=tk.StringVar(value=employee_details[0]))
        self.name_label.pack()
        self.name_entry.pack()

        self.position_label = tk.Label(self.border_frame, text="Position:", font=('Helvetica', 12, 'bold'), bg="#468B97", fg="white")
        self.position_entry = tk.Entry(self.border_frame, textvariable=tk.StringVar(value=employee_details[1]))
        self.position_label.pack()
        self.position_entry.pack()

        self.salary_label = tk.Label(self.border_frame, text="Salary:", font=('Helvetica', 12, 'bold'), bg="#468B97", fg="white")
        self.salary_entry = tk.Entry(self.border_frame, textvariable=tk.DoubleVar(value=employee_details[2]))
        self.salary_label.pack()
        self.salary_entry.pack()


        self.update_button = tk.Button(self.border_frame, text="Update", command=self.update_employee, bg="#1D5B79", fg="white")
        self.update_button.pack(pady=10)


        self.back_button = tk.Button(self.border_frame, text="Back", command=self.go_back, bg="#1D5B79", fg="white")
        self.back_button.pack(pady=10)

    def update_employee(self):

        new_name = self.name_entry.get()
        new_position = self.position_entry.get()
        new_salary = self.salary_entry.get()

        self.cursor.execute("UPDATE employees SET name=?, position=?, salary=? WHERE employee_id=?",
                            (new_name, new_position, new_salary, self.employee_id))


        self.conn.commit()
        self.conn.close()


        messagebox.showinfo("Success", "Employee details updated successfully!")


        self.refresh_employee_list()


        self.parent.destroy()

    def go_back(self):

        self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    update_employee_app = UpdateEmployeeApp(root, 1, lambda: None)  # Replace lambda function with your refresh_employee_list function
    root.mainloop()
