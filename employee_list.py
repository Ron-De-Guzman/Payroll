import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from addemployee import AddEmployeeApp
from updateemployee import UpdateEmployeeApp
from deleteemployee import DeleteEmployeeApp


class EmployeeListView:
    def __init__(self, root, go_back):
        self.root = root
        self.root.title("Employee List")
        self.root.configure(bg="#1D5B79")
        self.root.geometry("1500x700")

        self.go_back = go_back


        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'))
        self.style.configure("Treeview", font=('Helvetica', 10), rowheight=25)


        self.employee_tree = ttk.Treeview(root, columns=("Employee ID", "Name", "Position", "Salary"), show="headings")
        self.employee_tree.heading("Employee ID", text="Employee ID")
        self.employee_tree.heading("Name", text="Name")
        self.employee_tree.heading("Position", text="Position")
        self.employee_tree.heading("Salary", text="Salary")

        self.employee_tree.pack(pady=10)


        self.add_employee_button = tk.Button(root, text="Add Employee", command=self.open_add_employee)
        self.add_employee_button.pack(pady=10)

        self.back_button = tk.Button(root, text="Back", command=self.close_window)
        self.back_button.pack(pady=10)


        self.update_employee_button = tk.Button(root, text="Update Employee", command=self.open_update_employee)
        self.update_employee_button.pack(pady=10)


        self.delete_employee_button = tk.Button(root, text="Delete Employee", command=self.open_delete_employee)
        self.delete_employee_button.pack(pady=10)

        self.load_employee_list()

    def load_employee_list(self):

        conn = sqlite3.connect("employee_database.db")
        cursor = conn.cursor()


        cursor.execute("SELECT employee_id, name, position, salary FROM employees")
        employees = cursor.fetchall()


        for employee in employees:
            self.employee_tree.insert("", "end", values=(employee[0], employee[1], employee[2], employee[3]))


        conn.close()

    def close_window(self):
        self.root.withdraw()
        self.go_back()

    def open_add_employee(self):

        add_employee_window = tk.Toplevel(self.root)
        add_employee_app = AddEmployeeApp(add_employee_window, self.refresh_employee_list)

    def refresh_employee_list(self):

        self.employee_tree.delete(*self.employee_tree.get_children())
        self.load_employee_list()

    def open_update_employee(self):

        selected_item = self.employee_tree.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select an employee to update.")
            return


        employee_id = self.employee_tree.item(selected_item)["values"][0]


        update_employee_window = tk.Toplevel(self.root)
        update_employee_app = UpdateEmployeeApp(update_employee_window, employee_id, self.refresh_employee_list)


    def open_delete_employee(self):

        selected_item = self.employee_tree.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select an employee to delete.")
            return


        employee_id = self.employee_tree.item(selected_item)["values"][0]


        delete_employee_window = tk.Toplevel(self.root)
        delete_employee_app = DeleteEmployeeApp(delete_employee_window, employee_id, self.refresh_employee_list)



if __name__ == "__main__":
    root = tk.Tk()
    employee_list_view = EmployeeListView(root, root.iconify)
    root.mainloop()
