print( "        The application of user defined matrix using numpy modle        ")
import numpy as np


r =int(input("Enter the number of rows  "))
c =int(input("Enter the number of colums "))

mat =np.zeros(( c , r ),dtype=int)

print(len(mat)) # the lenght is basically the number of rows
print(mat) 

for i in range(r):
    for j in range(len(mat[i])):
        x=int(input("Enter the elements  "))
        mat[i][j]= x

print(mat)

for i in range( r ):
    for j in range(len(mat[i])):
        print("The row",i,"col",j,mat[i][j])
