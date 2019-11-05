






from tkinter import  *

root= Tk()

root.title("Lazy Buttons")

app=Frame(root)

app.grid()


#Create a Button in the frame

btn1=Button(app,text="I do nothing")
btn1.grid()

btn2=Button(app)
btn2.grid()

btn2.configure(text="Me Too")


btn3=Button(app)
btn3.grid()

btn3["text"]= "Same Here!"

#Kick of the window's event Loop


root.mainloop()
          
          
