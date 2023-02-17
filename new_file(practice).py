'''
def factorial(no):
    fac=0
    if no ==0 or no==1:             # ITS A TRAP
        return 1
    else:
        return no*factorial(no-1)
    
number =int(input(" ENTER THE VALUE YOU WANT    "))
print(factorial( number ))


def f(a):
    return a[1]

a= [[1,2],[0,0],[3,1]]

a.sort(key=f)
print(a)         # done
'''
def o(B):
    return lambda x:x[1]

B=[[1,2],[0,0],[3.1]]
B.sort(key= lambda x:x[2])
print(B)

