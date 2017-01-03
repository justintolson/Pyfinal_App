# Python Ver:   3.5
#
# Author:       Justin Tolson

#
# Purpose:      Your employer wants a program to move all his .txt files from one folder to another
#                with the click of a click of a button. On your desktop make 2 new folders. Call one Folder A &
#                the second Folder B. Create 4 random .txt files & put them in Folder A.
#
#Import libraries needed for this function
import os
import shutil

#Create the function and name the parameters
def file_mover( fromFilepath, toFilepath ):

    #Create a for loop search through Folder A
    for files in os.listdir(fromFilepath):

        #If any of the files in Folder A end with .txt, have them transferred to Folder B
        if files.endswith('.txt'):

            #Join the filepath with the files that to be transferred
            file_source = os.path.join(fromFilepath, files)

            file_destination = os.path.join(toFilepath, files)

            #shutil.move to transfer the files from Folder A to Folder B
            shutil.move(file_source, file_destination)

            #Print which files have been transferred
            print("Copied {} to {}".format(files, toFilepath))


file_mover("C:/Users/Justin/Desktop/Folder A", "C:/Users/Justin/Desktop/Folder B")