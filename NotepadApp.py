from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile,asksaveasfilename

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def selectall():
    textArea.event_generate("<<SelectAll>>")

def cut():
    textArea.event_generate("<<Cut>>")


def close():
    root.destroy()

def helpFunct():
    showinfo("Help !!!!","This Notepad has the functionality of copy and paste")

def aboutus():
    showinfo("About us !!!!", "This was developed by YCODZNOW")


def openFunct():
    path=askopenfile()
    f = open(path.name)
    data = f.read()
    f.close()
    textArea.insert(1.0,data)


def new():
    textArea.delete(1.0,END)

def save():
    savingPath = asksaveasfilename()
    content = textArea.get(1.0,END)
    f = open(savingPath,"w")
    f.write(content)
    f.close()




root = Tk()
root.geometry("500x300")
root.title("NoteX")
root.minsize(400,200)
root.maxsize(800,500)

mainMenu = Menu(root)
root.config(menu = mainMenu)


fileMenu = Menu(mainMenu,tearoff=0)
#so program widgets wont break while click or drag
fileMenu.add_command(label="Open",command=openFunct)
fileMenu.add_command(label="New",command=new)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="Quit",command=close)

editmenu = Menu(mainMenu,tearoff=0)
editmenu.add_command(label="Copy",command = copy)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Paste",command=paste)
editmenu.add_command(label="Select All",command=selectall)

aboutMenu = Menu(mainMenu,tearoff=0)
aboutMenu.add_command(label="Help",command=helpFunct)
aboutMenu.add_command(label="About Team",command=aboutus)


mainMenu.add_cascade(label="File",menu = fileMenu)
mainMenu.add_cascade(label="Edit",menu=editmenu)
mainMenu.add_cascade(label="About Us",menu=aboutMenu)
#display options
textArea = Text()
textArea.pack(expand=True,fill = BOTH)
#fill complete window
root.mainloop()


