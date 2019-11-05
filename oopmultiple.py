
class A:
       def  A(self):
               print('I am A')

class B:
        def  A(self):
              print('I am A in subclass')

        def  B(self):
              print('I am B')

class C(A,B):

         def  A(self):
               print('I am A in Class C')
         def  C(self): 
               print('I am C')
               

x=C( )
y=B( )
z=B( )
y.A( )
x.B( )
x.C( )
z.A( )
x.A( )





