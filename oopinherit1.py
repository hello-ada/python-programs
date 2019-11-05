


class  Firstclass:

          def setdata(self, value):
                   self.value=value

          def  display(self):
                     print(self.value)


class Secondclass(Firstclass):

           def  display(self):
                      print ("Current value = '%s '"%self .value)


x=Firstclass( )
y=Secondclass()
x.setdata("Computer Science")
x.display()
y.setdata("Electronics and Communication")
y.display()
