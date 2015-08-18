from tkinter import *
from tkinter import ttk
import csv

def wordChecker(*args):
    testWord=ourWord.get()
    file=open("words.csv", "rt")
    wordList=csv.reader(file)
    for oneWordList in wordList:
        word=oneWordList[0]
        word=word.encode("ascii","ignore")
        word=word.decode("utf-8")
        match=False
        if testWord==word:
            match=True
            break
    file.close()
    if match:
        answer.set(testWord+' is a match!')
    else:
        answer.set(testWord+' is not common :-(')
    
root = Tk()
root.title("Common word test:")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ourWord = StringVar()
answer = StringVar()

our_word_entry = ttk.Entry(mainframe, width=15, textvariable=ourWord)
our_word_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=answer).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Check for match", command=wordChecker).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

our_word_entry.focus()
root.bind('<Return>', wordChecker)

root.mainloop()
