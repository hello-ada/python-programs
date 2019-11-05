
first_number=input("Enter the first number.")
sec_number=input("Enter the second number")
try:
          num1=float(first_number)
          num2=float(sec_number)
          result=num1/num2
except  ValueError:
             print ("Two numbers are Required")
except ZeroDivisionError:
             print ("Zero can't be a denominator")
else:
              print(str(num1)  + "/" +str(num2) + "=" +str(result))
             
print(" after the exception block")
