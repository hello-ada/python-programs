
#Lazy Buttons 2
#Demonstrates using a Class  with Tkinter

from tkinter import  *

class Application(Frame):
    
      def  __init__(self,master):
                 Frame.__init__(self,master)
                 self.grid()
                 self.create_widgets()
          
      def create_widgets(self):
                 self.btn1=Button(self,text="I do Nothing")
                 self.btn1.grid()
                 self.btn2=Button(self)
                 self.btn2.grid()
                 self.btn2.configure(text="Me Too")
                 self.btn3=Button(self)
                 self.btn3.grid()
                 self.btn3["text"]="Same Here"


#main like method
root= Tk()
root.title("Lazy Buttons2")
app=Application(root)
app.grid()
root.mainloop()

