print('         ITERATIVE VALUES        ')
Z =('TALHA','AHMED','RANA','HASSAN','HAMZEE','KASHIF','DANIYAL','HUSNAIN','SOHIAB')

myiter = iter( Z )
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 
print(next(myiter))
print(next(myiter))
print(next(myiter))      # SIMPLE FOR LOOP SCENES

#       CAN ALSO WORK WITH THE STRING 
z1 = ' Muhammad Talha Zahid '
z2 ='Iphone 12 pro max'
myiter1 =iter( z1 )
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))   # AGAIN SIMPLE PRINTING AS DONE IN FOR LOOPS

#       SIMPLE ITER EXAMPLE CAN BE FOR LOOP 
print(" ")
for x in Z:
    print(x)

#   SIMILARLY 
for x in z2:
    print(x)


class math:
    def __iter__(self):
        self.x = 1 # initializing the value
        return self
    
    def __next__(self):
        a =self.x
        self.x += 1
        return a

myiter = math()   # object created
myiter1 = iter (myiter)
print(' ')
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))
print(next(myiter1))     # simple 1 to 13 i.e the number of times we printed the values
print(' ')
# simple iteration with limit

class mathematics:
    def __iter__(self):
        self.a = 1   # initializing the values
        return self
    def __next__(self):
        if self.a <=18:
             x =self.a
             self.a += 1
             return x
        else:
            raise StopIteration


my = mathematics()    #object created!!!! 
my1 =iter( my )
for x  in my:
    print(x)   # no need the value of x

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration      # raise -> no return always remember that

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)



print(" IN THE NEXT FUNCTION WE WOULD USE THE SCOPE OPERATORS OF EVERY MEHOD AVAIALABLE ")