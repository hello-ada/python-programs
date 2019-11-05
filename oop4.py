class Car(object):
#A simple attempt to represent a car.#
     def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
     def get_descriptive_name(self):
             long_name =  self.make + '  ' + self.model +'   '+str(self.year) 
             return long_name.title()

     def read_odometer(self):
         print("This car has  " + str(self.odometer_reading) + " miles on it.")

     def update_odometer(self, mileage):
                         if mileage >= self.odometer_reading:
                                self.odometer_reading = mileage
                         else:
                                print("You can't roll back an odometer!")


     def increment_odometer(self, miles):
                            self.odometer_reading += miles


mycar=Car('MMmotors','Maruti800',2016)
print("This car  Make Model and Year of manufacturing is" +'  '+ str(mycar.get_descriptive_name()) + " title on it.")
mycar.read_odometer()
mycar.update_odometer(20)
mycar.read_odometer()
mycar.increment_odometer(500)
mycar.read_odometer()

    
