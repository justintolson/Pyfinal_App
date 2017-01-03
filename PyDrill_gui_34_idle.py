from tkinter import *
import tkinter as tk

import PyDrill_gui_34_idle_main
import pydrill_gui_funcs


def load_gui(self):
    # define various labels and where they need to go within the grid
    self.lbl_fname = tk.Label(self.master,text='Browse')
    self.lbl_fname.grid(row=0, column=0,padx=(10,0),pady=(10,30))
    self.lbl_fname = tk.Label(self.master,text='Destination')
    self.lbl_fname.grid(row=4, column=0,padx=(10,0),pady=(10,30))
    self.lbl_fname = tk.Label(self.master,text='Submit')
    self.lbl_fname.grid(row=8, column=0,padx=(10,0),pady=(10,30))
    self.lbl_fname = tk.Label(self.master,text='Done')
    self.lbl_fname.grid(row=8, column=3,padx=(10,0),pady=(10,30))
    
    
    # description and location of each button that will appear in the gui
    self.btn_browse = tk.Button(self.master, width = 12, height = 2, text = 'Browse',
                                command=lambda: pydrill_gui_funcs.browse(self))
    self.btn_browse.grid(row=0,column=4,padx=(15,0),pady=(15,30))
    self.btn_destination = tk.Button(self.master, width = 12, height = 2, text = 'Destination',
                                     command=lambda: pydrill_gui_funcs.destination(self))
    self.btn_destination.grid(row=4, column=4, padx=(15, 0), pady=(15, 30))
    self.btn_submit = tk.Button(self.master, width = 12, height = 2, text = 'Submit',
                                command=lambda: pydrill_gui_funcs.file_mover(self, self.custom_source, self.custom_dest))
    self.btn_submit.grid(row=8, column=2, padx=(15, 0), pady=(15, 30))
    self.btn_done = tk.Button(self.master, width = 12, height = 2, text = 'Done',
                              command=lambda: pydrill_gui_funcs.done(self))
    self.btn_done.grid(row=8, column=4, padx=(15, 0), pady=(15, 30))
    
    
    # define the browse box and what info it will hold
    self.custom_source = StringVar()
    self.custom_source.set('Select a source directory')
    self.text_source = tk.Entry(self.master, width=60, textvariable=self.custom_source)
    self.text_source.grid(row=1, column=2, rowspan=1, columnspan=2, padx=(5, 0),
                          pady=(10, 20))
    
    
    # define the destination box and what info it will hold
    self.custom_dest = StringVar()
    self.custom_dest.set('Select a destination directory')
    self.text_dest = tk.Entry(self.master, width=60, textvariable=self.custom_dest)
    self.text_dest.grid(row=5, column=2, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))
















