print(" ZIP method of numpy ")

import numpy as np

a=[1,2,3,4,5,6]
b=[7,8,9,10,11,12]
c=[] # simple array

# using the zip function

for x,y in zip(a,b):
    c.append(x+y)
print("\n",c)   #simply prints the sum of each element of the array


z =zip(a,b)
print(list(z))# simply prints the list 

# important thing to note is that the if we simply print the zipped values of 2 arrays, the returned value is the address of the returned array rather than the content in it 
print(" ")
print(*z)


E =[90,28,181,371]
F=[91,1271,27189,1]
G =np.add(E ,F)
print("\n",G)
print(" ")
H =np.greater(E,F)
print(H)


# rounding off elements of the array understudy

J =[1.2,1.9,1.113,992.022]
k =np.rint(J)
print(" ")
print(k)