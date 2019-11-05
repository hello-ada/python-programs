





class MyError(Exception):
         #Constructor or Initializer
         def  __init__(self,value):
                self.value = value
         def  __str__(self):
                    return(repr(self.value))
try:
     raise(MyError(3*8))
          #Value of Exception is stored in  error

except MyError as  e:
                print('A new Exception occured: ', e.value)
