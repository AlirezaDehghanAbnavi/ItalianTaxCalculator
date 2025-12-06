"""Seperate class to organize title better"""
import tkinter as tk
from src.utils.paths import PHOTOS_DIR


class Title(tk.Label):
    """Defining a title for the calculator."""
    def __init__(self, parent):
        """Extending the Label from tkinter."""
        self.photo = tk.PhotoImage(file=PHOTOS_DIR/"Logo.png")


        super().__init__(
            parent,
            text="Welcome!\n" \
            "Use this tool to calculate your taxes accurately and efficiently.",
            font=("Arial", 20),
            bg="#E2D5A0",
            fg="black",
            relief=tk.RAISED,
            bd=5,
            padx=20,
            pady=20,
            image=self.photo,
            compound='top'
        )
