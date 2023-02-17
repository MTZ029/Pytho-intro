print("Arithematic operations using numpy ufunc")
import numpy as np

array1 =np.array([1,2,3,4,5,6,7,8,9,10])

array2=np.array([11,12,13,14,15,16,17,18,19,20])

# add()
new =np.add(array1 ,array2)
print("\n", new) #fact -> it just prints the even terms

# subtract()

new1 =np.subtract(array1 ,array2)

print("\n",new1)  # difference is printed simply 

# multiply()

new2 =np.multiply( array1 ,array2 )
print("\n",new2)

# divide()

new3 =np.divide(array1 , array2 )
print("\n", new3)
print(" ")
# power()

new4 =np.power(array1 ,array2)
print("\n",new4)

# mode ()

print("   ")
new5 =np.mod(array1 ,array2 )
print(new5) 

array3 =np.array([3,1,10,14,15])
array4 =np.array([2,3,4,5,6])
print("         ")
print("     ")
new6 =np.mod(array3 , array4)

print("\n",new6)

# raminder()     => would probably get the same results as we got in the mod function

print("     ")
new7 =np.remainder(array3 , array4)
print("we get the same result as we get in the mod function" ,new7)

# divmod()   => we are returned with two arrays that are 1st is the qoutient and second is the remiander


# syntax of the returned values=> (qoutient , mod)
print("     ")
new8 =np.divmod(array3 ,array4)
print("\n",new8)


# absolute()   => we use the function but not abs() so that we don't confuse it with math.abs() a in-builtin function of python
print("     ")
array5 =np.array([-213,12,2,-1,14,-12,-2,-3243,-3])
new9= np.absolute( array5 )
print("\n",new9)

