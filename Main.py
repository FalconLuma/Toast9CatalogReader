import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext

from FileReader import *

class Main:
    def __init__(self):
        self.label_file_explorer = None
        self.text_area = None
        self.fileReader = None

# Function for opening the
# file explorer window
    def openFile(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files", "*.txt*"),
                                                         ("all files", "*.*")))

        # Change label contents
        self.label_file_explorer.configure(text="File Opened: " + filename)
        self.fileReader = FileReader(filename)
        self.fileReader.parseFile()
        self.readDisk(45)

    def build(self):
        # Create the root window
        window = Tk()

        # Set window title
        window.title('File Explorer')

        # Set window size
        window.geometry("1000x500")

        # Set window background color
        window.config(background="white")

        # Create a File Explorer label
        self.label_file_explorer = Label(window,
                                    text="File Explorer using Tkinter",
                                    width=100, height=4,
                                    fg="blue")

        button_explore = Button(window,
                                text="Browse Files",
                                command=self.openFile)

        button_exit = Button(window,
                             text="Exit",
                             command=exit)

        # Grid method is chosen for placing
        # the widgets at respective positions
        # in a table like structure by
        # specifying rows and columns
        self.label_file_explorer.grid(column=1, row=1)

        button_explore.grid(column=1, row=2)

        button_exit.grid(column=1, row=3)

        self.text_area = scrolledtext.ScrolledText(window, width = 100, height = 20)
        self.text_area.grid(column=1,row=4)
        self.text_area.config(state='disabled')

        # Let the window wait for any events
        window.mainloop()

    def readDisk(self, index):
        disk = self.fileReader.getKeys()[index]
        #print(disk)
        entry = self.fileReader.disks[disk]

        for e in entry:
            self.text_area.config(state='normal')
            self.text_area.insert(tkinter.INSERT, (e.name+"\n"))
            self.text_area.config(state='disabled')
            #print(e.name)


if __name__ == "__main__":
    m = Main()
    m.build()
