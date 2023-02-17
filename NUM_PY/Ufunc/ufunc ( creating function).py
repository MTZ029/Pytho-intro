print("Dealing with the creating function method ")

# dealing with the frompufunc -> the following parameters ahould be taken care of 
# -> Function
# ->input 
# -> Output
# syntax   ===> (function,input ,output)
# simply define the universal function and the call/use it afterwards

import numpy as np
def sam(a , b):
    return a+b

my_add=np.frompyfunc(sam , 2, 1 )

print(" ")
print(my_add([1,2,3,4,5,6],[7,8,9,10,11,12]))

def Talha(p ,o,i):
    return p*o*i

my =np.frompyfunc(Talha , 3 , 1)

print(my([1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]))
# simple 

# defining the type of the function and the checking for the errors in the code for using a  undefined function

print(type(np.add))
print(type(np.concatenate))
# print(np.Talha) => simply pops an error that would say that the Talha is not a ufunc defined by python

# we can also print the weather the function is computer defined ufunc or not 
# np.ufunc -> can be used instead to check for its presence

print("     ")



if type(np.add) ==np.ufunc:
    print(True)
else:
    print(False)