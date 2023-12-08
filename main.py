import tkinter as tk
from login import LoginPage
from register import RegisterPage
from home import HomePage



class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main App")

        self.show_login()


    def show_login(self):
        self.clear_window()
        self.login_page = LoginPage(self.root, self.show_register, self.show_home)

    def show_register(self):
        self.clear_window()
        self.register_page = RegisterPage(self.root, self.show_login)

    def show_home(self):
        self.clear_window()
        self.home_page = HomePage(self.root, self.show_login)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
