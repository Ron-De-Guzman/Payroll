import tkinter as tk
from tkinter import messagebox
import sqlite3

class RegisterPage:
    def __init__(self, root, open_login):
        self.root = root
        self.root.title("Register Page")
        self.root.geometry("1500x700")
        self.root.configure(bg="#1D5B79")

        self.open_login = open_login


        self.register_frame = tk.Frame(root, pady=150, padx=150, bd=5, relief=tk.GROOVE, bg="#468B97")
        self.register_frame.place(relx=0.5, rely=0.5, anchor="center")


        self.register_text = tk.Label(self.register_frame, text="Register", font=('Helvetica', 20, 'bold'), bg="#468B97", fg="white")


        self.username_label = tk.Label(self.register_frame, text="Username:", font=('Helvetica', 12), bg="#468B97", fg="white")
        self.username_entry = tk.Entry(self.register_frame, font=('Helvetica', 12))


        self.password_label = tk.Label(self.register_frame, text="Password:", font=('Helvetica', 12), bg="#468B97", fg="white")
        self.password_entry = tk.Entry(self.register_frame, show="*", font=('Helvetica', 12))


        self.register_button = tk.Button(self.register_frame, text="Register", command=self.register, font=('Helvetica', 12))


        self.login_button = tk.Button(self.register_frame, text="Login", command=self.open_login, font=('Helvetica', 12))


        self.register_text.grid(row=0, column=0, columnspan=2, pady=10)
        self.username_label.grid(row=1, column=0, pady=10, sticky="e")
        self.username_entry.grid(row=1, column=1, pady=10, padx=10)
        self.password_label.grid(row=2, column=0, pady=10, sticky="e")
        self.password_entry.grid(row=2, column=1, pady=10, padx=10)
        self.register_button.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        self.login_button.grid(row=3, column=1, pady=55, padx=55, sticky="e")

    def register(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()


        conn = sqlite3.connect("user_database.db")
        cursor = conn.cursor()


        cursor.execute("SELECT * FROM users WHERE username=?", (entered_username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Error", "Username already exists. Please choose another.")
        else:

            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (entered_username, entered_password))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registration successful! You can now login.")
            self.open_login()

if __name__ == "__main__":
    root = tk.Tk()
    register_page = RegisterPage(root, root.quit)
    root.mainloop()
