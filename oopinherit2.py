class Car():
                  #A simple attempt to represent a car."""
        def __init__(self, make, model, year):
                 self.make = make
                 self.model = model
                 self.year = year

        def get_descriptive_name(self):
                   long_name = str(self.year) + ' ' + self.make + ' ' + self.model
                   return long_name.title()

class ElectricCar(Car):

        def __init__(self, make, model, year):
       ##Initialize attributes of the parent class."""
                super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
