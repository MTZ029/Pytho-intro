import sys
print("First assignment of the python")
print("NOTE THAT NO NEED TO INITIALISE THE VALUES LIKE INT , FLOAT , CHAR etc")

#                                      FOR LOOP AND HOW TO USE IT WITH INTEDATIONS
for i in range(4):
    print("Pakistan")
    print(i)
print("outside the loop")

x=20
#                                       PRINTING THE VALUE OF X
print(x)
#                                       PRINTING THE DATA TYPES
print(type(x))
#                               we use the integers when the simple counting is envolved

y=x+0.5
d=19.6
print(d)
print(type(d))
print(y)
print(type(y))
#                                      we us float for decimal figures

z="Hello World"
print(z)
print(type(z))
za="03315889192"
print(za)
print(type(za))
# can;t do this
# p=za+1
#print(p)
#   We use sting because the character data type doesn't exist and we can use the numbers but we can't add them or any arithematric operations

q=4+2j
qa=q+1j
print(q)
print(type(q))
print(qa)
print(type(qa))
#                   Simple addition like complex numbers, the complex is used when the complex plain is used

a=["Talha","Sohaib","Kashif",5]
print(a)
print(type(a))
a[2]="talha"
print(a)

m=["talha",45,1j]

i,u,y,r=["Talha","Sohaib","Kashif",5]
print(u)


A=[("talha",87,"talha",87,87,87,9j+29,29+9j)]     # type of list
print(A)
print(type(A))
#                                               Simple list
#                      ->The paranthesis [brackets] are important
#                      ->The values are mutable, thus the values can change, as shown in the code above
#                      ->The list take large size for the same data as the tuple
#                      ->List supports packing in one sack but doesn't supports unpacking as shown in the code above


b=("qau","electronics","5th")
print(b)
print(type(b))
#                                   like a list but the differences are
#                      ->The paranthesis are not as important, thus the lack of brackets would remain tuple
#                      ->The values cannot be changed, thus immutable, as dhwon in the code below

o="talha","pakistan",4j,9
print(o)
print(type(o))
n="talha",45,1j
print(sys.getsizeof(n))
print("byte")
print(sys.getsizeof(m))
print("byte")
v,c,x="talha","pakistan",9+4j
print(x)
#o[1]="Python"
#print(o)   CAUSES AND ERROR

pa=range(8)
for g in range(9):
    print(g)
print(pa)
print(type(pa))
#                                The range is basically a list that flows like loop simply
 
sa={"talha",87,"talha",87,87,87,9j+29,29+9j}
print(sa)
#sa[4]=86 immutable
#print(sa)
print(type(sa))
# The set uses the curly brackets 
# the set takes account of the repeating value and lets the value to be printed once as shown in the code above

Q={"name":"Talha","age":20,"height":"6"}
W={'name':'Waqas','age':11,'weight':50}
print(W)
Q['name']='sohaib'
print(Q)
print(type(Q))
print(sys.getsizeof(Q))
print(sys.getsizeof(W))

e={"name":"pak","cell":1133,"name":"Talha"} #duplicate keys. note in this case the pair would be name:talha
print(e)
print(type(e))
#dictionary is used to make the key value pairs 
#the dictionary like set uses curly bracket otherwise is same.

vow='aeiou'
#note that the value passed in this case is string & it is called the iteration
#iterations are of following type: 1->string 2->list 3->tuple 4->dictionary 5->set
sac={'day':'SUNDAY','date':25,'month':'July','Year':2022} 
#dictionary ->note that only the keys are passsed as shown in the code below:
fs=frozenset(vow)
print(fs)
print(type(fs))
F=frozenset(sac)
print(F)
print(type(F))

T,f=True,False
print(T,f)
print(type(T),type(f))
#                                boolean as shown above is the value that differentiates between true and false.

L=[150,250,20,34]
b=bytes(L)
print(b[0],b)
print(type(b))
D=["Talha","Pakistan","Asia","Indian ocean"]
print(D[2])
d=[0,1,2,3,4]
c=bytes(d) 
#c[0]=1 Immutable
print(c)
#Immutable sequence of bytes from 0 to 256

I=[150,199,255,239]   #hexa decimal addressess
z=bytearray(I)
print(z[3])
print(type(z))
z[3]=113
print(z[3])
#mutable sequence of bytes from 0 to 256

i=None
print(i)
print(type(i))
# Used when the variable should be empty completely, thus the when a variable is equal to zero, the variable cam't  be called empty

u=[16,32,44]
r=bytes(u)
mv=memoryview(r)
print(type(mv))
print(mv)
print(sys.getsizeof(mv))

p=20,30,40,50
k=bytes(p)

mv1=memoryview(k)
print(mv1)
#note that the memory view will only work on the bytes and other than that, the memory view lets us know the object's internal data without any copy paste.