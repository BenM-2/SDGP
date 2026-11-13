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

        self.geometry("1000x600") if not responsive_window \
            else f"{int(self.winfo_screenwidth() * 0.8)}x{int(self.winfo_screenheight() * 0.8)}"

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