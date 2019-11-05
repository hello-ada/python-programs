

class A:
        i=123
        
        def __init__(self):
                 self.i=345
                 self.j=540

print(A.i)                #calling i through class variable.
print(A().i)
x=A()
print(x.j)
print(x.i)


