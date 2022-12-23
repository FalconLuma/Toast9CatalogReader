import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext

from FileReader import *

class Main:
    def __init__(self):
        self.label_file_explorer = None
        self.disk_text_area = None
        self.fileReader = None

    def build(self):
        # Create the root window
        window = Tk()

        # Set window title
        window.title('File Explorer')

        # Set window size
        window.geometry("1000x800")

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

        self.label_file_explorer.grid(column=1, row=1, columnspan=3)

        button_explore.grid(column=1, row=2, columnspan=3)

        button_exit.grid(column=1, row=3, columnspan=3)

        self.textbox = Text(window,height=1,width=80, wrap='none')
        self.textbox.grid(column=1,row =4,columnspan=2)
        button = Button(window,text="search",command=self.search)
        button.grid(column=3, row = 4)

        self.disk_text_area = scrolledtext.ScrolledText(window, width = 30, height = 40)
        self.disk_text_area.grid(column=1, row=5)
        self.disk_text_area.config(state='disabled')

        self.file_text_area = scrolledtext.ScrolledText(window, width=110, height=40)
        self.file_text_area.grid(column=2, row=5, columnspan=2)
        self.file_text_area.config(state='disabled')

        window.mainloop()

    def openFile(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files", "*.txt*"),
                                                         ("all files", "*.*")))

        # Change label contents
        self.label_file_explorer.configure(text="File Opened: " + filename)
        self.fileReader = FileReader(filename)
        self.fileReader.parseFile()

    def search(self):
        self.disk_text_area.config(state='normal')
        self.disk_text_area.delete('1.0', 'end')
        self.disk_text_area.config(state='disabled')

        self.file_text_area.config(state='normal')
        self.file_text_area.delete('1.0', 'end')
        self.file_text_area.config(state='disabled')

        string = self.textbox.get('1.0', 'end').strip('\n')
        strings = string.split(sep=',')

        found = dict()
        for k in self.fileReader.disks.keys():
            for e in self.fileReader.disks[k]:
                en = e.name.lower()
                matches = [False for _ in range(len(strings))]
                for i, s in enumerate(strings):
                    s = s.strip()
                    s = s.lower()
                    s0 = ' ' + s + ' '
                    s1 = ':' + s + ' '
                    s2 = ' ' + s + ':'
                    s3 = ':' + s + ':'
                    if (s0 in en) or (s1 in en) or (s2 in en)or (s3 in en):
                        matches[i] = True

                fullMatch = True
                for b in matches:
                    if b == False:
                        fullMatch = False

                if fullMatch == True:
                    try:
                        v = found[k]
                        v.append(e)
                        found[k] = v
                    except KeyError:
                        found[k] = [e]
                fullMatch = True
        print("search done")
        self.printSearch(found)

    def printSearch(self, results):
        sep = "--------------------------------------------------------------------------------------------------------------"

        self.disk_text_area.config(state='normal')
        self.disk_text_area.insert(tkinter.INSERT, ("Matching Disks:\n"))
        self.disk_text_area.config(state='disabled')
        currentPath = []
        for k in results.keys():
            self.disk_text_area.config(state='normal')
            self.disk_text_area.insert(tkinter.INSERT, (k + "\n"))
            self.disk_text_area.config(state='disabled')

            for e in results[k]:
                en = e.name
                path = en.split(':')
                path.pop()
                if not path == currentPath:
                    self.file_text_area.config(state='normal')
                    for f in path:
                        self.file_text_area.insert(tkinter.INSERT, (f + "/"))
                    self.file_text_area.insert(tkinter.INSERT, ("\n"))
                    self.file_text_area.config(state='disabled')
                    currentPath = path

            self.file_text_area.config(state='normal')
            self.file_text_area.insert(tkinter.INSERT, (sep + "\n"))
            self.file_text_area.config(state='disabled')

    def wordIn(self, word, phrase):
        return word in phrase.split()

if __name__ == "__main__":
    m = Main()
    m.build()
