from unittest import result


print("         FUNCTIONS       ")
#           block of code that runs when it is called 
#           you an pass the data as a parameter into a function
#           a function can return data as a result 
#           in python a function is defined by using the def function

def myfunc():
    print("     THIS IS MY FIRST FUNCTION       ")

def f(age):
    print("     The age is  ",age)
myfunc()       # THE VALUES IN IT GET PRINTED 

def name(f_name):
    print(f_name + 'Zahid')

print(" ")
name('Talha')     # simply used witht the functions that are defined by us! we are concerned aboout the values inside
print(" ")
f(20)

# function with multiple arguments
def triple(name,sex,age):
    print(' THE BIO IS ->AGE IS ',age,' ->THE SEX IS ',sex,' ->THE NAME IS ',name)

triple('Muhammad Talha Zahid','MALE',20)


#           WHEN THE NUMBER OF ARGUMENTS ARE UNKNOWN OF A FUNCTION, ADD *
def children(*_child):
    print(" The youngest child is "+_child[3])
# important thing to remember is that we need to know the number of arguments overall, the child[2] would let you know the last prinited argument of the function
# another thing to note is that we need to specify the indexing in order to remove the error
children('talha','momina','taha','Ahmed')    

print(" ")
def cars(*_mycar):
    print(" The last car I bought is ",_mycar[3])
cars('hyundai','toyota','zuzuki','Kia')

print(" ")
def inst(inst1 , inst2 , inst3, inst4):
    print(" the last institute is ",inst4)
inst ("Bahria",'Fizaya','NUST','QAU')

#           Note that WE CAN USE ** IF WE WANT THE ARGUMENTS AND THE KEYS ARE UNKNOWN AS SHOWN BELOW:
print(" ") 
def honda(**cars):
    print(" THE LATEST CAR IF HONDA IS ",cars['car4'])  # note that the car4 is the name of the key being used 
honda(car1='city',car2='civic',car3='Jade',car4='vezel')

#               SIMPLE IS THAT, WE CAN MAKE THE ARGUMENT IS DEFAULT 

def fun(country = 'Pakistan'):
    print(" I AM FROM ",country)
fun()
print(" ")
fun('India')

food=list(('Biryani','Apple','Leechee','Orange'))
def myfood(food):
    for x in food:      # for loop to print all the elements of food
        print(x)
myfood(food)

print(" ")
Dosti=list(('Talha','zaid','umer','Saqib'))
def dost(Dosti):
    for x in Dosti:
        print(x)
dost(Dosti)

#           FUNCTION WITH A RETURN STATEMENT 
def sumfun(x):
    return 5 * x            #doesn't print in this version of python

#x2=input("entrer the value to be multiplied with 5  ")
# sumfun(x2)


# function with pass statement to remove the errors from the function while execution of the interpreter

def my_function():
    pass

my_function


print(" ")
#           FUNCTION RECURSION -> THIS MEANS THAT WE USE THE SAME FUNCTION INSIDE THE FUNCTION

"""def func(str1):
    func(str1)
    print("the value is ",str1)

func( 13 )""" # Error
print(" ")
# simple exampke of recursion is fatorial 
numbers=int( input(" enter the nbumber of fac "))

def factorial(n):
    fac =1       #local to the function
    for i in range(n):
        fac = fac * (i+1)
    return fac
    #pass

print("factorial via iteratrive method is ",factorial(numbers))      # we need to print when we use the return function



def factorial_recurcive(j):
    if j==0 or j==1 :
        return 1
    else:
        return j * factorial_recurcive(j-1)

num = int(input("enter the value you want to take factorial of  "))    # type casting 
print(factorial_recurcive( num ))    # print used cuz of return used in the functio defined1


def fibonacci_sequence(n):# finonacci 0 1 1 2 3 5 8 13
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

no =int(input("   enter the amount you want to search fibonacci for  "))
print(fibonacci_sequence(no))

                   
# got it 


"""
def polo_recursion(k):
    if (k > 10):
        result = k + polo_recursion(k-1)     # simply calling the function again
    else:
        result =0                               # ask DrMusarat
    return result   # NOT PRINTING DON'T KNOW WHY  
print(" ")
print(polo_recursion( 14 ))  """