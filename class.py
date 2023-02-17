print(' THIS IS THE FUNCTION OF CLASS   ')

class talha:
    x = 5

y = talha()
print(y.x)      # y is my object and x is my value I want to print

class bio:
    def __init__(self,name,age ):#  NoTE THAT THT ESELF IS ALWAYS PRESENT IN it
         self.name = name 
         self.age = age
        
    
b1 =bio("   TALHA  ",20)
print(b1.name,' ',b1.age)         # simple 


#  IMPORTANT THING TO REMEBER IS THAT WE ALWAYS DEFINE THE NEW FUNCTION UNDER THE CLASS DEFINED

class boy:
    def __init__(self,father,age) :
        self.father = father 
        self.age = age 

    def my(self):
        print(" THE FATHER NAME IS ",self.father)

p1 =boy('Zahid',50)
print(p1.age)
p1.my()

#           the self attribute can be changed if we want to 
class stu:
    def __init__(silly,name,age):   # no marks conotation marks
        silly.name = name
        silly.age = age   
    def n(abc):
        print(" THE NAME IS "+abc.name)
    def r(abc):
        print(" THE REGISTRATION IS "+abc.age) 

p2=stu('TALHA','29') 
p2.n()
p2.r()   # note that we can't print the integer value without the conotation marks on it  check for the pycharm 


# CHANGING THE VALUES FROM THE FUNCTIOIN
p2.age ='40'
print(p2.age)      # simple

# delete function
del p2.name
#       print(p2.name)   # error
#   NOTe THAT WE CAN ALSO DELETE THE OBJECT CREATED 
del p2
#print(p2)  error

#       IF WE WANT TO REMOVE THE ERROR FROM A EMPTY CLASS, USE PASS => SAME
class hyundai:
    pass
# no error
