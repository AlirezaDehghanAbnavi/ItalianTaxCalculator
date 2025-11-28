import tkinter as tk


class Counter(tk.Label):
    def __init__(self, parent, initial=0):
        super().__init__(
            parent,
            text=f"Count: {initial}",
            font=("Arial", 18, "bold"),
            bg="#123456",
            fg="white"
        )
    

    def onClick(self, newCount):
        self.config(text=f"Count: {newCount}")
        print(f"Incrementing count: {newCount}!")