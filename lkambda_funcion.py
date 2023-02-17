print('     LAMBDA FIUNCTION        ')
#               IMPORTANT ->A SPECIAL TYPE OF FUCTION
#                         -> LAMBDA IS THE KEY WORD
#                         ->CAN TAKE ANY NUMBER OF ARGUMENTS BUT ONLY ONE EXPRESSION => EXPLAINED IN THE ALTER SCENARIOS

no =int(input("Enter the number     "))
x =lambda a : a*2
print(x(no))                    #   PRINT FUNCTION IS ENVOKED AS SHOWN

#       CAN TAKE ANY NUMBER OF ELEMENTS BUT DOESN'T SUPPORT UNPACKING

no1 =int(input('enter the 1st value'))
no2 =int(input('enter the 2nd value'))
no3 =int(input('enter the 3rd value'))
x1 =lambda a,b,c : a*b+c
print('\n',x1(no1,no2,no3))     #   SIMPLE FUNCTION



#       note that the real use of lambda function is when we call the function inside the other function

#   syntax
def fun(n):
    lambda a : n -a     #simple 

# original example

"""def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
	
print(mydoubler(11)) """

def func( n ):
    return lambda a : a*n     # Note THAT ERROR WAS DUE TO RETURN 
    print( n )

myfunc = func( 2 )    # THIS IS THE VALUE OF N => THIS IS THE FUNCTION THAT IS DEFINED

print(myfunc(10))

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
v=int(input("   ENTER THE VALUE OF ARGUMENT FOR THE FUNCTION    "))
NUMBER1=int(input(" ENTER THE VALUE OF V    "))
def funt(no):
    return lambda a : a + no
another = funt(v) 
print(another(NUMBER1))

#    Note THAT WE KNOW THE WE CAN ALSO USE MORE THAN ONE ARDUMENT OF THE FUNCTION
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
def name(talha):
    return lambda a:a*talha
f =name(2)
f =name(3)


print(f(10))
print(f(20))

#       CHECK THE PRACTICE FILE FOR THE LAST LIST OPERATION
