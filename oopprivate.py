class  Critter(object):
         def __init__(self,name):
                 print("A new critter has been born")
                 self.__name = name


         def get_name(self):
                 return self.__name




crit=Critter("BMSCE")
print(crit.get_name())
