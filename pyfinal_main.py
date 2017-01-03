# import various libraries as needed
from tkinter import *
import tkinter as tk

# import gui and functions pages
import pyfinal_gui
import pyfinal_funcs


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        # define the minimum window size
        self.master.minsize(600,400)
        # define the maximum window size
        self.master.maxsize(800,600)
        # define the title for the master frame
        self.master.title("UI for File Transfer")
        # define the color for the master frame
        self.master.configure(bg="#4E5552")

        pyfinal_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()






