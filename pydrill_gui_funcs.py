from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import datetime
import shutil

import PyDrill_gui_34_idle
import PyDrill_gui_34_idle_main


def browse(self):
    self.text_source.delete(0, 60)
    self.custom_source = filedialog.askdirectory()
    self.text_source.insert(0, self.custom_source)


def destination(self):
    self.text_dest.delete(0, 60)
    self.custom_dest = filedialog.askdirectory()
    self.text_dest.insert(0, self.custom_dest)


def file_mover(self, fromFilepath, toFilepath ):

    now = datetime.datetime.now()
    ago = now - datetime.timedelta(hours=24)

    for files in os.listdir(fromFilepath):

        if files.endswith('.txt'):
            filepath = os.path.join(fromFilepath, files)
            st = os.stat(filepath)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)

            if mtime > ago:
                file_source = os.path.join(fromFilepath, files)
                file_destination = os.path.join(toFilepath, files)

                shutil.move(file_source, file_destination)

                print("Copied {} to {}".format(files, toFilepath))


def done(self):
    if messagebox.askokcancel("Exit Program",
                              "Are you sure you want to close the application?"):
        self.master.destroy()
        os._exit(0)

