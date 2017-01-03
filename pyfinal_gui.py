
from tkinter import *
import tkinter as tk
import time

import pyfinal_funcs


def load_gui(self):
    # define various labels and where they need to go within the grid
    self.lbl_fname = tk.Label(self.master,text='Search directory for file')
    self.lbl_fname.grid(row=0, column=2,padx=(10,0),pady=(10,30))
    self.lbl_fname = tk.Label(self.master,text='Choose folder to receive file')
    self.lbl_fname.grid(row=4, column=2,padx=(10,0),pady=(10,30))
    self.lbl_fname = tk.Label(self.master,text='Press submit to transfer file')
    self.lbl_fname.grid(row=8, column=1,padx=(10,0),pady=(10,30))

    # define various buttons that appear within the GUI and specify what happens when each button is clicked
    self.btn_search = tk.Button(self.master, width = 12, height = 2, text = 'Search',
                                command=lambda: pyfinal_funcs.search(self))
    self.btn_search.grid(row=0,column=4,padx=(15,0),pady=(15,30))
    self.btn_destination = tk.Button(self.master, width = 12, height = 2, text = 'Destination',
                                     command=lambda: pyfinal_funcs.destination(self))
    self.btn_destination.grid(row=4, column=4, padx=(15, 0), pady=(15, 30))
    self.btn_submit = tk.Button(self.master, width = 12, height = 2, text = 'Submit',
                                command=lambda: pyfinal_funcs.file_mover(self, self.custom_search, self.custom_dest))
    self.btn_submit.grid(row=8, column=2, padx=(15, 0), pady=(15, 30))
    self.btn_done = tk.Button(self.master, width = 12, height = 2, text = 'Done',
                              command=lambda: pyfinal_funcs.finished(self))
    self.btn_done.grid(row=8, column=3, padx=(15, 0), pady=(15, 30))

    # define the search box and what info it will hold
    self.custom_search = StringVar()
    self.custom_search.set('Select a source directory')
    self.text_search = tk.Entry(self.master, width=60, textvariable=self.custom_search)
    self.text_search.grid(row=1, column=2, rowspan=1, columnspan=2, padx=(5, 0),
                          pady=(10, 20))

    # define the destination box and what info it will hold
    self.custom_dest = StringVar()
    self.custom_dest.set('Select a destination directory')
    self.text_dest = tk.Entry(self.master, width=60, textvariable=self.custom_dest)
    self.text_dest.grid(row=5, column=2, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

    pyfinal_funcs.create_db(self)













