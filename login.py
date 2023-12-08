import tkinter as tk
from tkinter import messagebox
import sqlite3

class LoginPage:
    def __init__(self, root, open_register, open_home):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1500x700")
        self.root.configure(bg="#1D5B79")

        self.open_register = open_register
        self.open_home = open_home


        self.login_frame = tk.Frame(root, pady=150, padx=150, bd=5, relief=tk.GROOVE, bg="#468B97")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")


        self.login_text = tk.Label(self.login_frame, text="Login", font=('Helvetica', 20, 'bold'), bg="#468B97", fg="white")


        self.username_label = tk.Label(self.login_frame, text="Username:", font=('Helvetica', 12), bg="#468B97", fg="white")
        self.username_entry = tk.Entry(self.login_frame, font=('Helvetica', 12))


        self.password_label = tk.Label(self.login_frame, text="Password:", font=('Helvetica', 12), bg="#468B97", fg="white")
        self.password_entry = tk.Entry(self.login_frame, show="*", font=('Helvetica', 12))


        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, font=('Helvetica', 12))


        self.register_button = tk.Button(self.login_frame, text="Register", command=self.open_register, font=('Helvetica', 12))

        self.login_text.grid(row=0, column=0, columnspan=2, pady=10)
        self.username_label.grid(row=1, column=0, pady=10, sticky="e")
        self.username_entry.grid(row=1, column=1, pady=10, padx=10)
        self.password_label.grid(row=2, column=0, pady=10, sticky="e")
        self.password_entry.grid(row=2, column=1, pady=10, padx=10)
        self.login_button.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        self.register_button.grid(row=3, column=1, pady=55, padx=55, sticky="e")

    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        print("Entered Username:", repr(entered_username))
        print("Entered Password:", repr(entered_password))

        if not entered_username or not entered_password:
            messagebox.showerror("Error", "Please enter both username and password")
            return


        conn = sqlite3.connect("user_database.db")
        cursor = conn.cursor()


        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (entered_username, entered_password))
        user = cursor.fetchone()

        conn.close()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.open_home()
        else:
            messagebox.showerror("Error", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root, root.quit, root.quit)
    root.mainloop()
