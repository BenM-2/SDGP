"""
@ Author:        George Dawson
@ Date:          13/11/2026
@ Name:          gui.py
@ Description:   This file contains the implementation of the GUI class for the delivery package. The GUI class is responsible for creating and managing the graphical user interface of the application using the CustomTkinter library.
"""


# TODO: change navigation from left to top
#       get heartbeat wokring
#       work on error management
#       experiment with asyncio


from . import *


class LeftSidebar(ctk.CTkFrame):
    """Left sidebar for navigation and options"""
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self, text="Navigation", font=ctk.CTkFont(size=18, weight="bold")
        ).grid(row=0, column=0, padx=15, pady=20, sticky="w")

        for row, name in enumerate(("Dashboard", "Algorithms", "Routes", "Settings"), start=1):
            ctk.CTkButton(
                self, text=name, command=lambda n=name: print(f"Selected: {n}")
            ).grid(row=row, column=0, padx=10, pady=5, sticky="ew")

    def update_frame(self, dt: float):
            # Update animations or visualisations
            pass


class MainPanel(ctk.CTkFrame):
    """Main panel for displaying content"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            self, text="Main Workspace", font=ctk.CTkFont(size=20, weight="bold")
        ).grid(row=0, column=0, padx=20, pady=15, sticky="w")

        self.workspace = ctk.CTkFrame(self)
        self.workspace.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="nsew")

        ctk.CTkLabel(
            self.workspace, text="Algorithm visualisation goes here"
        ).pack(expand=True)

    def update_frame(self, dt: float):
            # Update animations or visualisations
            pass


class RightSidebar(ctk.CTkFrame):
    """Right sidebar for properties and settings"""
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self, text="Properties", font=ctk.CTkFont(size=18, weight="bold")
        ).grid(row=0, column=0, padx=15, pady=20, sticky="w")

        ctk.CTkLabel(
            self, text="Route Settings"
        ).grid(row=1, column=0, padx=15, pady=5, sticky="w")

        ctk.CTkEntry(
            self, placeholder_text="Route name"
        ).grid(row=2, column=0, padx=15, pady=5, sticky="ew")

    def update_frame(self, dt: float):
        # Update animations or visualisations
        pass


class Gui(ctk.CTk):
    """Main GUI class for the delivery application"""
    SIDEBAR_WIDTH = 220
    MIN_CENTRE_WIDTH = 350

    TARGET_FPS = 60
    FRAME_TIME = 1.0 / TARGET_FPS

    def __init__(self, responsive_window: bool = True):
        super().__init__()

        self.title("SDGP")
        self.geometry("1200x750")
        self.minsize(500, 400)

        if responsive_window:
            self.after(100, self.set_responsive_size)

        self.left_visible = True
        self.right_visible = True

        # Column	        Weight	    Behaviour
        # Left sidebar	    0	        Keeps its preferred width
        # Centre workspace	1	        Expands to occupy extra space
        # Right sidebar	    0	        Keeps its preferred width

        # Three-column layout
        self.grid_columnconfigure(0, weight=0, minsize=self.SIDEBAR_WIDTH)
        self.grid_columnconfigure(1, weight=1, minsize=self.MIN_CENTRE_WIDTH)
        self.grid_columnconfigure(2, weight=0, minsize=self.SIDEBAR_WIDTH)

        # Toolbar + content
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # Top toolbar
        self.toolbar = ctk.CTkFrame(self, height=45, corner_radius=0)
        self.toolbar.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.toolbar.grid_propagate(False)

        ctk.CTkButton(
            self.toolbar, text="☰", width=40,
            command=self.toggle_left
        ).pack(side="left", padx=8, pady=5)

        ctk.CTkButton(
            self.toolbar, text="Properties", width=100,
            command=self.toggle_right
        ).pack(side="right", padx=8, pady=5)

        # Panels
        self.left = LeftSidebar(self)
        self.left.grid(row=1, column=0, sticky="nsew")

        self.main = MainPanel(self)
        self.main.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.right = RightSidebar(self)
        self.right.grid(row=1, column=2, sticky="nsew")

        self.running = True
        self.last_frame = time.perf_counter()

        self.after(0, self.heartbeat)
        self.protocol("WM_DELETE_WINDOW", self.on_close)    # custom window close protocol, to stop heartbeat and close window

        self.bind("<Configure>", self.on_resize)

        self.fps_label = ctk.CTkLabel(self, text="FPS: 0")
        self.fps_label.grid()


    def on_resize(self, event):
        if event.widget is not self:
            return

        width = event.width

        if width < 900:
            self.right.grid_remove()
            self.grid_columnconfigure(2, minsize=0)
        elif self.right_visible:
            self.grid_columnconfigure(2, minsize=self.SIDEBAR_WIDTH)
            self.right.grid()


    def on_close(self):
        self.running = False
        self.destroy()


    def heartbeat(self):
        if not self.running:
            return

        frame_start = time.perf_counter()

        dt = frame_start - self.last_frame
        self.last_frame = frame_start

        self.update_gui(dt)

        elapsed = time.perf_counter() - frame_start
        delay = max(1, round((self.FRAME_TIME - elapsed) * 1000))

        self.after(delay, self.heartbeat)


    def update_gui(self, dt: float):
        fps = 1 / dt if dt > 0 else 0

        self.fps_label.configure(
            text=f"FPS: {fps:.1f}"
        )

        self.left.update_frame(dt)
        self.main.update_frame(dt)
        self.right.update_frame(dt)


    def set_responsive_size(self):
        width = int(self.winfo_screenwidth() * 0.8)
        height = int(self.winfo_screenheight() * 0.8)
        self.geometry(f"{width}x{height}")


    def toggle_left(self):
        self.left_visible = not self.left_visible

        if self.left_visible:
            self.grid_columnconfigure(0, minsize=self.SIDEBAR_WIDTH)
            self.left.grid()
        else:
            self.left.grid_remove()
            self.grid_columnconfigure(0, minsize=0)


    def toggle_right(self):
        self.right_visible = not self.right_visible

        if self.right_visible:
            self.grid_columnconfigure(2, minsize=self.SIDEBAR_WIDTH)
            self.right.grid()
        else:
            self.right.grid_remove()
            self.grid_columnconfigure(2, minsize=0)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    app = Gui()
    app.mainloop()