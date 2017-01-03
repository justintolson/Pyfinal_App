# Python Ver:   3.5

# Author:       Justin Tolson


# Purpose:      Users are asking for a user interface to make using the script easier and more versatile.
#               Desired features of the UI:
#                Allow the user to browse to and choose a specific folder that will contain the
#               files to be checked daily.
#                Allow the user to browse to and choose a specific folder that will receive the
#               copied files.
#                Allow the user to manually initiate the 'file check' process that is performed by
#               the script.

# import various libraries as needed
from tkinter import *
import tkinter as tk

# import gui and functions pages
import PyDrill_gui_34_idle
import pydrill_gui_funcs


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        # define the minimum window size
        self.master.minsize(600,400)
        # define the maximum window size
        self.master.maxsize(600,400)
        # define the title for the master frame
        self.master.title("UI for File Transfer")
        # define the color for the master frame
        self.master.configure(bg="#B0B3A8")

        PyDrill_gui_34_idle.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()






