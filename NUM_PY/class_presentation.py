print("     Presentation            ")
import numpy as np
import numpy.linalg as la

a=np.array([[1,2],[3,4]])
det =la.det(a)
print("Determinant ", det)

print(" ")

ainv =la.inv(a)
print(ainv)

d , v =la.eig( a )
print( d )
print(" ")
print(v)

A =np.array([[1,2],[3,4]])
B =np.array([5,6])

Ainv =la.inv(A)
P =np.matmul( Ainv , B)
print(P)

G =la.solve( A , B)
print(G)

D =np.array([[1,2],[3,4],[7,8]])
e=np.array([[5],[6],[9]])

X =la.lstsq(D , e ,rcond =None)[0]
print( X )

r =int(input("Enter the number of rows "))
c=int(input("Enter the numbe rof columns "))

mat =np.zeros((r , c ),dtype=int )
print( mat )

for i in range( r ):
    for j in range(len(mat[i])):
        x =int(input("Enter the values   "))
        mat[i][j]=x

print(mat)

matrices =[[int(input(" Enter the value    "))for i in range(r)]for j in range( c )]
print( matrices)