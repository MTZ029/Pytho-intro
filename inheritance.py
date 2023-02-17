print('     INHERITANCE         ')

# simple class
class bio:
    def __init__(self,fname,lname):
        self.fname =fname
        self.lname =lname
    def func(self):
        print(self.fname,self.lname)
    
x =bio('talha','zahid')
x.func()       # simple

#   NOW PLAYING WITH INHERITED CLASS:
class bio1(bio):
    pass

x1 =bio1('Muhmmad ','Talha')
x1.func()

#       note that the init function is not considered while it is introduced in the child class

class bio2(bio):
    def __init__(self, fname, lname):
        bio.__init__(self,fname,lname)

x3 =bio2('MUNEEZA','FARUKH')
x3.func()       # simple 

###             ANOTHER CLASS -PARent & CHILD 
#      self() function is used to not use the parent nam whike calling the init -> CALLED AUTOMAITCALLY
class car:
    def __init__(self,cname,brandname,model):
        self.cname =cname
        self.brandname =brandname
        self.model =model
    def funt(self):
        print("The car name is",self.cname,' The brand name is ',self.brandname,' The model is ',self.model)

x2 =car('City','Honda','2007')
x2.funt()

class car1(car):
    def __init__(self, cname, brandname, model,manufacturingcountry):
        super().__init__(cname, brandname, model)   # super cuz no need of name of parent class
        self.manufacturingcountry = manufacturingcountry
x4 =car1('CIvic','HONDA',2007,'japan')
x4.funt()
print(' ')            # simple 
print(x4.manufacturingcountry)

# check for the pycharm for practice problem too 
    