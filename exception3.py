filename = 'facto.py'

try:
       with open(filename) as f_obj:
          contents = f_obj.read()
          print(contents)

except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)



        
        
