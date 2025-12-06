"""Launcher for the Italian Tax Calculator GUI."""
from src.components.window import MainWindow


def main():
    """Main body."""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
