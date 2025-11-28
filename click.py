import tkinter as tk

class Click(tk.Button):
    def __init__(self, parent, text, command=None):
        super().__init__(
            parent,
            text=text,
            font=('Ink Free', 20, 'bold'),
            bg='#ff6200',
            fg='#fffb1f',
            activebackground="#C13131",
            activeforeground='#fffb1f',
            command=command
        )