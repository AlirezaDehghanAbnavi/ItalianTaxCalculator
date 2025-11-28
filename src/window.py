import tkinter as tk
from title import Title
from click import Click
from counter import Counter


class MainWindow(tk.Tk):   # JAVA -> Class MainWindow extendes tk.Tk
    def __init__(self
                 ):    # JAVA -> Constructor MainWindow(){}
        super().__init__()
 

        self.geometry("620x520") # Determines size
        self.title("Italian Tax Calculator") # Title
        self.config(background="#123456") # Set Background Color


        # Set New Icon
        icon = tk.PhotoImage(file='.\\photos\\italia.png') 
        self.iconphoto(True, icon)


        # Displaying title label
        self.titleLable = Title(self)
        self.titleLable.pack()


        # Displaying counter label
        self.count = 0
        self.counterLabel = Counter(self, self.count)
        self.counterLabel.pack()


        # Button
        self.button = Click(self, "Click me", command=self.countIncrement)
        self.button.pack()


    def countIncrement(self):
        self.count += 1
        self.counterLabel.onClick(self.count)
        