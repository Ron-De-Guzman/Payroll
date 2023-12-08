

import tkinter as tk
from tkinter import messagebox
import sqlite3

class DeleteEmployeeApp:
    def __init__(self, parent, employee_id, refresh_employee_list):
        self.parent = parent
        self.parent.title("Delete Employee")
        self.parent.configure(bg="#1D5B79")
        self.parent.geometry("1500x700")


        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x_coordinate = (screen_width - 300) // 2
        y_coordinate = (screen_height - 150) // 2
        self.parent.geometry(f"300x150+{x_coordinate}+{y_coordinate}")

        self.employee_id = employee_id
        self.refresh_employee_list = refresh_employee_list


        self.conn = sqlite3.connect("employee_database.db")
        self.cursor = self.conn.cursor()


        self.cursor.execute("SELECT name FROM employees WHERE employee_id=?", (self.employee_id,))
        employee_name = self.cursor.fetchone()[0]


        self.message_label = tk.Label(parent, text=f"Are you sure you want to delete {employee_name}?", font=('Helvetica', 12), bg="#1D5B79", fg="white")
        self.confirm_button = tk.Button(parent, text="Delete", command=self.delete_employee, bg="#468B97", fg="white")
        self.cancel_button = tk.Button(parent, text="Cancel", command=self.cancel_delete, bg="#468B97", fg="white")


        self.message_label.pack(pady=10)
        self.confirm_button.pack(pady=5)
        self.cancel_button.pack(pady=5)

    def delete_employee(self):

        self.cursor.execute("DELETE FROM employees WHERE employee_id=?", (self.employee_id,))


        self.conn.commit()
        self.conn.close()


        messagebox.showinfo("Success", "Employee deleted successfully!")


        self.refresh_employee_list()


        self.parent.destroy()

    def cancel_delete(self):

        self.conn.close()
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    delete_employee_app = DeleteEmployeeApp(root, 1, lambda: None)  # Replace lambda function with your refresh_employee_list function
    root.mainloop()
