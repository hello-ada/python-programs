try:
      f=open('exception1.py')
      if f.name == 'exception1.py':
               raise Exception
except  FileNotFoundError as e:
      print('Sorry.This file does exist')
except Exception as e:
      print('Error!')
#except  FileNotFoundError as e:
#    print("This file does'nt exist")
else:
       print(f.read())
       f.close()
finally:
        print("Executing Finally...")
