print("         Trying to work on the user defined matrix with input options     ")

def Matrix():   # function define 
    r =int(input("Enter the number of rows "))
    c =int(input("Enter the number of columns "))
    mat =[ ] # defining a empty list for making a matrix

    for i in range(0 , r):
        mat.append([ ])  # simply used to append the list with the entries in the rows.

    for i in range(0 , r):
        for j in range(0 , c):
            mat[ i ].append(j) # Simply appendation of the rows and columns in the matri undertudy
            mat[i][j] = 0 # basic intialization

    for i in range(0 , r):
        for j in range(0 , c):
            print("Kindly Enter the elements for the rows", i+1," Column ",j+1 )
            mat[i][j]=int(input()) 
    print(mat)
    print(" ")

    x = input("Enter Y to make a new matrix of ypur own Other wise enter N")

    if x == 'N' or x =='n':
        print("Thankyou for trying")
    elif x =='Y' or x=='y':
        Matrix()
    else:
        print("Wront entry")
        exit( )

Matrix()

        #############################################################################################################
        ############### Another code for the same perpose one line code with applications  ##########################
    
col =int(input("Enter the number of columns for the matrix   " ))
row = int(input("Enter the number of rows for the matrix    "))
matrics =[[int(input())for i in range(col)]for j in range(row)] # simple we use the list in list method
print(" The second code applications ")
print(matrics)