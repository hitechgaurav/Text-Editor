from tkinter import *
from tkinter import filedialog

class Texteditor:
    curr_filecheck="no_file"

    def new_file(self):
        #New file open dialog box
        self.text.delete(1.0,END)
        self.curr_filecheck="no_file"
    def open_file(self):
        #Open dialog box command
        open_return=filedialog.askopenfile(initialdir="C:/Users/Gaurav SINGH/Desktop",title="Select As",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
        if(open_return!=None):
            self.text.delete(1.0,END) #Deleting texts after opening of new file from line 1 to end

            for line in open_return:
                self.text.insert(END,line)
        #closing a file when opened
            self.curr_filecheck=open_return.name
            open_return.close()
    def save_as(self):
        #Save As command
        path=filedialog.asksaveasfile(mode="w", defaultextension=(".txt"))
        if path is None: #If Cancel button is pressed
            return
        clipboard=self.text.get(1.0,END) #Taking all the data from text editor to clipboard
        self.curr_filecheck=path.name
        path.write(clipboard) #Writing clipboard to file extension

    def save(self):
        if self.curr_filecheck=="no_file":
            self.save_as()
        path=open(self.curr_filecheck, "w")
        path.write(self.text.get(1.0,END))
        path.close()

    def copy(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())
    def cut(self):
        self.copy()
        self.text.delete("sel.first","sel.last")
    def paste(self):
        self.text.insert(INSERT,self.text.clipboard_get())
    def __init__(self,root):
        self.root=root
        root.title("Notepad")
        root.geometry("1024x720")
        self.text=Text(self.root,undo=True,font=('Times New Roman',15))
        self.text.pack(fill=BOTH, expand=1)
        self.menu=Menu()
        self.root.config(menu=self.menu)
        #Creating File MENU
        self.file_menu= Menu(self.menu,tearoff=False)
        self.menu.add_cascade(label='File',menu=self.file_menu)
        self.file_menu.add_command(label="New",command=self.new_file)
        self.file_menu.add_command(label='Open',command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save As",command=self.save_as)
        self.file_menu.add_command(label='Save',command=self.save)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',command=top.destroy)
        #Creating Edit Menu

        self.edit_menu=Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='Edit',menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut",command=self.cut)
        self.edit_menu.add_command(label="Copy",command=self.copy)
        self.edit_menu.add_command(label="Paste",command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo",command=self.text.edit_undo)
        self.edit_menu.add_command(label="Redo",command=self.text.edit_redo)

top=Tk()
object=Texteditor(top)
top.mainloop()
