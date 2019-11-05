



class Box():
                  #A simple attempt to represent a car."""
        def __init__(self, width, height, length):
                 self.width = width
                 self.height = height
                 self.length= length

        def get_Cal_volume(self):
                   vol= self.width * self.height  * self.length
                   return vol

class Boxdemo(Box):

        def __init__(self, width, height, length):
       ##Initialize attributes of the parent class."""
                super().__init__(width, height, length)


my_tesla = Boxdemo(20,30,40)
final=my_tesla.get_Cal_volume()
print(final)
