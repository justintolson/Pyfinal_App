# import various libraries as needed
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import datetime
import shutil
# import gui and main pages
import PyDrill_gui_34_idle
import PyDrill_gui_34_idle_main

# clears text in search box/ Enables user to search directory/ Returns filepath into browse box
def browse(self):
    self.text_source.delete(0, 60)
    self.custom_source = filedialog.askdirectory()
    self.text_source.insert(0, self.custom_source)


# clears text in destination box/ enables user to search directory/ returns filepath into destination box
def destination(self):
    self.text_dest.delete(0, 60)
    self.custom_dest = filedialog.askdirectory()
    self.text_dest.insert(0, self.custom_dest)


# using two parameters "fromFilepath and "toFilepath" transfers files ending in ".txt" that have been updated within
# the last 24 hours from the "Browse" filepath to the "Destination" filepath
def file_mover( fromFilepath, toFilepath ):
    # establishes current time and subtracts 24 hours to be compared with ".txt" files being transferred
    now = datetime.datetime.now()
    ago = now - datetime.timedelta(hours=24)
    # loops through "fromFilepath" parameter to locate all files ending in ".txt"
    for files in os.listdir(fromFilepath):

        if files.endswith('.txt'):
            filepath = os.path.join(fromFilepath, files)
            st = os.stat(filepath)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            # compares timestamp on ".txt" file with the current time, minus 24 hours to determine if file has been
            # recently updated or not. if it has been updated within the last 24 hours the file is
            # transferred
            if mtime > ago:
                file_source = os.path.join(fromFilepath, files)
                file_destination = os.path.join(toFilepath, files)
                # transfers file from one folder to another
                shutil.move(file_source, file_destination)
                # prints which file was transferred and to which folder it was transferred to
                print("Copied {} to {}".format(files, toFilepath))

# when user clicks on "Done" a messagebox appears asking if they are sure they want to close application
def done(self):
    if messagebox.askokcancel("Exit Program",
                              "Are you sure you want to close the application?"):
        self.master.destroy()
        os._exit(0)

