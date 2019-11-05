




class  Firstclass:
          def setdata(self, value):
                   self.data=value

          def  display(self):
                     print(self.data)

class Secondclass(Firstclass):
           def  display(self):
                      print ("Current value = '%s '"%self .data)

class ThirdClass (Secondclass ) :
          def __init__( self , value ):
                           self . data = value
          def __add__( self , other):
                           return ThirdClass ( self .data + other )
          def __mul__( self , other):          
                            self . data = self . data * other


a = ThirdClass("abc")                          #new __init__ c a l l e d
a .display()
b = a + " xyz "                                       #new __add__ c a l l e d : makes a new instance
b.display()

a*3                                                         ##new __mul__ c a l l e d : changes i n s t a n c e in− p lace
a.display()

