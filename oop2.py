





class Animal():
          def __init__(self, name, age):
                             self.name=name
                             self.age=age
          def sit(self):
                         #Simulate a dog sitting in response to a command.#
                         print(self.name.title() + " is now sitting.")

          def roll_over(self):
                              #Simulate rolling over in response to a command#
                         print(self.name.title() + " rolled over!")


my_pet = Animal('willie', 6)
print("My dog's name is " + my_pet.name.title()+ ".")
print("My dog is " + str(my_pet.age) + " years old.")
my_pet.sit()
my_pet.roll_over()
