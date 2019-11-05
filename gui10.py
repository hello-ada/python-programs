





from tkinter import *

root=Tk()
app=Menu(root)
root.config(menu=app)
filemenu=Menu(app)
app.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='Exit')
helpmenu=Menu(app)
app.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()

