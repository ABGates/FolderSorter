# this script launches a program to sort a specified folder based on file type

import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def sortFiles():
    # convert user input to be useful
    location = entryBox.get()
    location = location.replace('\\', '/')
    if location[-1] != '/':
        location += '/'

    folders = []
    # iterate through folder in a context manager
    try:
        with os.scandir(location) as contents:
            for file in contents:
                # check if file is a folder
                if file.name.find('.') == -1:
                    folders.append(file.name)
                # if it is not a folder then do
                else:
                    fileType = file.name.rsplit('.', 1)[-1]
                    # move to fileType folder, or create new fileType folder then add
                    if fileType in folders:
                        shutil.move(location + file.name, location + fileType)
                    else:
                        try:
                            os.mkdir(location + fileType)
                        except FileExistsError:
                            pass
                        folders.append(fileType)
                        shutil.move(location + file.name, location + fileType)
    except FileNotFoundError:
        errorLabel.grid(row=8, column=5)
        return

    messagebox.showinfo("Success!", "Folder " + location + " was sorted")



# initiate GUI
window = Tk()
window.geometry("450x150")



def launchHelp():
    messagebox.showinfo("Help","This program will sort all files at the provided file location by file-type. It will create folders for each file-type present and place files of that type into that new folder")


def browseFolders():
    folderName = filedialog.askdirectory(initialdir = "C:/",title="Select a Folder")
    entryBox.select_clear
    entryBox.insert(0,folderName)


# define widgets
helpMenu = Button(window, text="Help",command=launchHelp)
titleLabel = Label(window, text="Folder Sorter")

eboxLabel = Label(window, text="Folder Path")
entryBox = Entry(window, width=40)
sort = Button(window, text="Sort", command=sortFiles)
browseButton = Button(window, text = "Browse",command=browseFolders)

errorLabel = Label(window, text="Error: could not find folder at that file path")

# place widgets in window
helpMenu.grid(row=0, column=0)
titleLabel.grid(row=5, column=5)
eboxLabel.grid(row=6, column=4)
entryBox.grid(row=6, column=5)
sort.grid(row=7, column=5)
browseButton.grid(row=6, column=6)

window.mainloop()
