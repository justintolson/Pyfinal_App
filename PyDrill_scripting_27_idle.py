# Python Ver:   3.5

# Author:       Justin Tolson


# Purpose:      To create a script that will automate the task of transferring files which have been edited within the
#               last 24 hours from their original folder, to a destination folder.

# Import all necessary libraries

import os
import shutil
import datetime

# Create a function to identify all files in 'Folder A' ending in .txt that have also been modified within the last 24
# hours

def file_mover( fromFilepath, toFilepath ):

    # loop through "fromFilepath" to locate all files ending in ".txt"

     for files in os.listdir(fromFilepath):

        if files.endswith('.txt'):

            file_source = os.path.join(fromFilepath, files)
            file_destination = os.path.join(toFilepath, files)
            now = datetime.datetime.now()
            ago = now - datetime.timedelta(hours=24)
            st = os.stat(file_source)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)

            # compares timestamp on ".txt" file with the current time, minus 24 hours to determine if file has been
            # recently updated or not. if it has been updated within the last 24 hours the name of the file is
            # transferred and its name printed along with the current timestamp on that file

            if mtime > ago:

                shutil.move(file_source, file_destination)

               print("Copied {} to {}".format(files, toFilepath))

file_mover("c:/users/justin/desktop/Folder A", "c:/users/justin/desktop/Folder B")
