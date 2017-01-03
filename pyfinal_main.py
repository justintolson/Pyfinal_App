# Python Ver:   3.5
#
# Author:       Justin Tolson
#
# Purpose:      You have been asked to implement this functionality. This means that you will need to
#               • create a database and a table
#               • modify your script to both record date/time of 'file check' runs and to retrieve that data for use in
#               the 'file check' process, and
#               • modify the UI to display the last 'file check' date/time

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






