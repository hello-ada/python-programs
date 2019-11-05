



from tkinter import *

class  Application(Frame):

        def __init__(self,master):
                  Frame.__init__(self,master)
                  self.grid()
                  self.btn_clicks=0
                  self.create_widget()

        def create_widget(self):
                  self.bttn=Button(self)
                  self.bttn["text"]="Total clicks 0"
                  self.bttn["command"]=self.update_count    #Event Handler
                  self.bttn.grid()

        def update_count(self):
                 self.btn_clicks+=1
                 self.bttn["text"]="Total clicks : "+str(self.btn_clicks)


 #main
root=Tk()
root.title("Click counter")
app=Application(root)
root.mainloop()
