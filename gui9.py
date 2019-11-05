from tkinter import   *







class Application(Frame):
        def  __init__(self,master):
                    Frame.__init__(self,master)
                    self.grid()
                    self.create_widgets()

        def   create_widgets(self): 
                     Label(self,text="Choose your Favourite Movie Types").grid(row=0,column=0,sticky=W)
                     Label(self,text="Select one:").grid(row=1,column=0,sticky=W)
                    #Create variable for  single,favourite  type of movie
                     self.favourite=StringVar()
                    #Create Comedy Radio Button
                     Radiobutton(self,text="Comedy",variable=self.favourite,value="comedy",command=self.update_text).grid(row=2,column=0,sticky=W)
                     Radiobutton(self,text="Drama", variable=self.favourite,value="drama",command=self.update_text).grid(row=3,column=0,sticky=W)
                    #Create  Text field to display Result
                     self.results_txt=Text(self,width=40,height=5,wrap=WORD)
                     self.results_txt.grid(row=5,column=0,columnspan=3)
                   
        def  update_text(self):
                     msg="Your favorite type of movie is "
                     msg+=self.favourite.get()
                     self.results_txt.delete(0.0,END)
                     self.results_txt.insert(0.0,msg)


                   


root=Tk()
root.title("Movie Chooser 2")
app = Application(root)
root.mainloop()
                           
