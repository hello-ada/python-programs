print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")


first_number = input("\nFirst number: ")
second_number = input("\nSecond number: ")
##print("After the While Loop")
try:
       answer = int(first_number) / int(second_number)
except ZeroDivisionError:
        print("You can't divide by 0!")
else:  
        print(answer)
print("After the Exception Block")
