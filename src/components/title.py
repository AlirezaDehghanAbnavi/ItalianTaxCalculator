"""Seperate class to organize title better"""
import tkinter as tk


class Title(tk.Label):
    """Defining a title for the calculator."""
    def __init__(self, parent):
        """Extending the Label from tkinter."""
        self.photo = tk.PhotoImage(file='./photos/Logo.png')


        super().__init__(
            parent,
            text="Welcome!\n" \
            "You can calculate your taxes here",
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
