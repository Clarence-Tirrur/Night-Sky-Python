import tkinter as tk
from tkinter import messagebox


class LoginWindow:

    def __init__(self, dm, success_callback):

        self.dm = dm
        self.success_callback = success_callback

        self.root = tk.Tk()
        self.root.title("Login")

        tk.Label(self.root, text="Username").pack()
        self.username = tk.Entry(self.root)
        self.username.pack()

        tk.Label(self.root, text="Password").pack()
        self.password = tk.Entry(self.root, show="*")
        self.password.pack()

        tk.Button(
            self.root,
            text="Login",
            command=self.login
        ).pack()

    def login(self):

        username = self.username.get()
        password = self.password.get()

        if self.dm.validate_login(username, password):

            self.root.destroy()
            self.success_callback(username)

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password"
            )

    def run(self):
        self.root.mainloop()
