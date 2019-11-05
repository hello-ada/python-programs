from tkinter import   *






class Application(Frame):
        def  __init__(self,master):
                    Frame.__init__(self,master)
                    self.grid()
                    self.create_widgets()

        def   create_widgets(self): 
                    Label(self,text="Choose your Favourite Movie Types").grid(row=0,column=0,sticky=W)
                    Label(self,text="Select all that apply:").grid(row=1,column=0,sticky=W) 
                    self.likes_comedy=BooleanVar()
                    self.res=Checkbutton(self, text="Comedy",variable=self.likes_comedy,command=self.update_text)
                    self.res.grid(row=2,column=0,sticky=W)
##                    self.likes_drama=BooleanVar()
##                    self.res1=Checkbutton(self, text="Drama",variable=self.likes_drama, comand=self.update_text1)
##                    self.res1.grid(row=3,column=0,sticky=W)
##                    self.likes_romance=BooleanVar()
##                    Checkbutton(self, text="Romance",variable=self.likes_romance,comand=self.update_text).grid(row=4,column=0,sticky=W)
                    self.results_txt=Text(self,width=40,height=3,wrap=WORD)
                    self.results_txt.grid(row=7,column=0,columnspan=3)
##                    Text(self,width=40,height=5,wrap=WORD).grid(row=7,column=0,columnspan=3)
                    

        def  update_text(self):
                     likes = ""
                     if self.likes_comedy.get():
                                     likes+="You Like  comedic movies.\n"
##                     if self.likes_drama.get():
##                                     likes+="You like Drama Movies.\n"
##                 if self.likes_romance.get():
##                                     likes+="You Like Romantic Movies.\n"
                     self.results_txt.delete(0.0,END)
                     self.results_txt.insert(0.0,likes)


                   


root=Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()
                           
