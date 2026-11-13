"""
@Author:        George Dawson
@Date:          13/11/2026
@Name:          gui.py
@Description:   This file contains the implementation of the GUI class for the delivery package. The GUI class is responsible for creating and managing the graphical user interface of the application using the CustomTkinter library.
"""

from . import *

class Gui(ctk.CTk):
    def __init__(self, responsive_window: bool=False) -> None:
        """
        Initialise the GUI application

        :param responsive_window: If set to True, the default window size will be responsive to active display size
        :return: None
        """
        super().__init__()
        self.title("SDGP")
        # Set the window size to 80% of the screen size if responsive_window is True

        if responsive_window:
            width = int(self.winfo_screenwidth() * 0.8)
            height = int(self.winfo_screenheight() * 0.8)
            self.geometry(f"{width}x{height}")
            
        else:
            self.geometry("1000x600")

        self.resizable(True, True) # sets window to resizable

        # Create a label
        self.label = ctk.CTkLabel(self, text="Hello, CustomTkinter!")
        self.label.pack(pady=20)

        # Create a button
        self.button = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)


    def on_button_click(self):
        self.label.configure(text="Button Clicked!")


if __name__ == "__main__":
    app = Gui(responsive_window=True)
    app.mainloop()