from tkinter import *
import os

def filechoose():
    def fileopen(ev=None):
        item=files.get(files.curselection())
        if os.path.isdir(item):
            os.chdir(item)
            filelist()
        elif os.path.isfile(item):
            content.delete(1.0,END)
            content.insert(1.0,open(item,'r').readlines())
            contentlabel.config(text=item)
            filewin.destroy() 
            
    def filelist():
        files.delete(0,END)
        files.insert(END,'.')
        files.insert(END,'..')
        for item in os.listdir():
            files.insert(END,item)
        filewin.update()

    filewin=Toplevel(top)

    files=Listbox(filewin)
    files.pack()
    filelist()
    files.bind('<Double-1>',fileopen)
    
    ok=Button(filewin,text='OK',command=fileopen)
    ok.pack()

top=Tk()
top.geometry('250x250')

MyMenu=Menu(top,tearoff=0)
MyMenu.add_command(label='Open',command=filechoose)
top.config(menu=MyMenu)

contentlabel=Label(top,text='file:')
contentlabel.pack()
content=Text(top)
content.insert(INSERT,'choose a file')
content.pack()

mainloop()
