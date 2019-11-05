



class  Firstclass:

          def setdata(self, value):
                   self.__data=value

          def  display(self):
                     print(self.__data)


class Secondclass(Firstclass):

           def  display(self):
                      print ("Current value = '%s '"%self.data)


x=Firstclass( )
y=Secondclass()
x.setdata("Computer Science")
x.display()
y.setdata("Electronics and Communication")
y.display()
