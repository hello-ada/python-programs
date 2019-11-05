class C1():
    
          def f1(self,id1):
                  self.id1=id1
                  print(self.id1)

          def f2(self,id2):		
                  self.id2=id2
                  print(self.id2)


              
# create C1 instances
myc1=C1( )
myc1a=C1( )

# call f2 method on one instance
myc1.f1(35)
myc1a.f2(90)
