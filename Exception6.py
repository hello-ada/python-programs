import math


class BMSNumberError(Exception):
       #Attempted improper operation on negative  number
        pass

def squareRoot(number):
        #Computes Square Root of number .Raises Negative Number Error if number is less than 0
 try:
        if number < 0:
             raise(BMSNumberError)
 except BMSNumberError as e:
            print("BMS Number")
 else:
        return math.sqrt(number)




x=squareRoot(-78)
print(x)

