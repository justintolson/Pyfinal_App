# import various libraries as needed
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import datetime
import shutil
import sqlite3
import time

# import gui and main pages
import pyfinal_gui
import pyfinal_main


# clears text in search box/ Enables user to search directory/ Returns filepath into search box
def search(self):
    self.text_search.delete(0, 60)
    self.custom_search = filedialog.askdirectory()
    self.text_search.insert(0, self.custom_search)


# clears text in destination box/ enables user to search directory/ returns filepath into destination box
def destination(self):
    self.text_dest.delete(0, 60)
    self.custom_dest = filedialog.askdirectory()
    self.text_dest.insert(0, self.custom_dest)


# connects with database and creates table if it doesn't already exist
def create_db(self):
    conn = sqlite3.connect("pyfinal.db")
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS file_transfer(unix REAL)")
        conn.commit()
        c.close()
    conn.close()


# update/browse through existing table
    def update_db(self):
        conn = sqlite3.connect("pyfinal.db")
        with conn:
            c = conn.cursor()
            c.execute("SELECT MAX(unix) FROM file_transfer")
            most_recent = c.fetchone()[0]
            most_recent = time.ctime(most_recent)
            c.close()
        conn.close()

        # displays in the UI the last 'file check' date/time
        self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
        self.label_print.grid(row=10, column=1, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

    update_db(self)


# using two parameters "fromFilepath and "toFilepath" transfers files ending in ".txt" that have been updated within
# the last 24 hours from the "Search" filepath to the "Destination" filepath
def file_mover(self, fromFilepath, toFilepath):
    # establishes current time and subtracts 24 hours to be compared with ".txt" files being transferred
    now = datetime.datetime.now()
    ago = now - datetime.timedelta(hours=24)
    print('The following .txt files were modified in the last 24 hours: \n')
    # loops through "fromFilepath" parameter to locate all files ending in ".txt"
    for files in os.listdir(fromFilepath):

        if files.endswith('.txt'):
            filepath = os.path.join(fromFilepath, files)
            st = os.stat(filepath)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            # compares timestamp on ".txt" file with the current time, minus 24 hours to determine if file has been
            # recently updated or not. if it has been updated within the last 24 hours the file is
            # transferred and its name printed along with the current timestamp on that file
            if mtime > ago:
                print('{} ~ last modified {}'.format(filepath, mtime))
                file_source = os.path.join(fromFilepath, files)
                file_destination = os.path.join(toFilepath, files)
                # transfers file from one folder to another
                shutil.move(file_source, file_destination)
                # prints which file was transferred and to which folder it was transferred to
                print("Copied {} to {}".format(files, toFilepath))

    # enters current time into database when click event occurs
    current_time = time.time()
    conn = sqlite3.connect("pyfinal.db")
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO file_transfer VALUES({})".format(current_time))
        conn.commit()
        c.close()
    conn.close()
    # displays a tkinter message box letting the user know that files were transferred successfully
    messagebox.showinfo("File Transfer", "File successfully transferred!")

    # update/browse through existing table
    def update_db(self):
        conn = sqlite3.connect('pyfinal.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT MAX(unix) FROM file_transfer")
            most_recent = c.fetchone()[0]
            most_recent = time.ctime(most_recent)
            c.close()
        conn.close()

        # displays in the UI the last 'file check' date/time
        self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
        self.label_print.grid(row=10, column=1, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))


    update_db(self)


# when user clicks on "Done" a messagebox appears asking if they are sure they want to close application
def finished(self):
    if messagebox.askokcancel("Exit Program",
                              "Are you sure you want to close the application?"):
        self.master.destroy()
        os._exit(0)




