print('     SCOPE OPRATION ->LOCAL AND GLOBAL VARIABLES RELATIVE TO THE FUNCTIONS               ')

# NOte THAT THE FUNCTION INSIDE THE FUNCTION -> LOCAL AND GLOBAL VARIABLE 
# these are the functions of local variable
def male():
    x =3000
    print(x)
male()     #         DONE WITH IT 

def myfunc():
    x =20000
    def myfunct1():
        print(x)
    myfunct1()        # THE OBJECT OF THE INTERNAL FUNCTION
myfunc() # THE OBJECT OF THE EXTERNMAL; FUNCTION

# these are the variables that are global

y =4050
def talha():
    y=2031
    print(y)
talha()
print(' ')
print(y)            # simply same variables 

def mal():
    global i       # = 321314 is error
    i = 321314
    print(i)
     
mal()
print(" THE VARIABELS IF GLOBAL ",i)     # ok to understand
print('  ')
r = 200
def tal():
    global r
    r = 300
    print(r)

tal()    # the value of r is updated
print(r)