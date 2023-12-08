import tkinter as tk
from tkinter import messagebox

from addemployee import AddEmployeeApp


class HomePage:
    def __init__(self, root, logout):
        self.root = root
        self.root.title("Home Page")

        self.logout = logout

        self.label = tk.Label(root, text="Welcome to the PHILIPPINES!", bg="#468B97", fg="white", font=('Helvetica', 24, 'bold'))
        self.label.pack(pady=10)

        self.view_employee_list_button = tk.Button(root, text="View Employee List", command=self.open_employee_list)
        self.view_employee_list_button.pack(pady=10)

        self.logout_button = tk.Button(root, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)


    def open_employee_list(self):
        from employee_list import EmployeeListView  # Import moved here
        self.root.withdraw()  # Hide the home page
        employee_list_root = tk.Toplevel(self.root)
        employee_list_view = EmployeeListView(employee_list_root, self.go_back_home)

    def go_back_home(self):
        self.root.deiconify()  # Show the home page again

if __name__ == "__main__":
    root = tk.Tk()
    home_page = HomePage(root, root.quit)
    root.mainloop()
