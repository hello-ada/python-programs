





try:
       a= input("Enter the Integer Number")
       a=int(a)
       if a<4:
               #throws ZeroDivisionError for a =3
                  b=a/(a-3)
       
                  print("Value of b= ",b)
       else:
                 print("Value of a =",a)

except(ZeroDivisionError):
                  print("\n Error Occurred and Handled")

                  print("After the exception has  caught")
        
