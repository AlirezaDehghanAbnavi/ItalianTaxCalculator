import tkinter as tk


class Title(tk.Label):
    def __init__(self, parent):
        self.photo = tk.PhotoImage(file='.\\photos\\Logo.png')


        super().__init__(
            parent,
            text="Welcome!",
            font=("Arial", 20),
            bg="#123458",
            fg="white",
            relief=tk.RAISED,
            bd=5,
            padx=20,
            pady=20,
            image=self.photo,
            compound='top'
        )
