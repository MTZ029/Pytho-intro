print(" tuples  " )

friends=('Talha','Hassan','Hamzee','Kashif','Husnain','Sohaib','Ahmed','Daniyal','Rana')
fruits = ("apple","Mango","Leechee","Orange")
numbers=(33,44,11,22,43,55,12,21,31)
Boolea=(True,False,True,False,True,True,False,False,True)  #    ALLOWS duplication
cars=('toyota','honda','suzuki','BMW','mercedes','audi','hyundai')
print(friends,'\n',numbers,'\n',Boolea)

# lenght function
print(len(friends)) # simple as list 

#   Note that if you want one input argument in the tuples, use the comma otherwise it would be considered string
x=('Talha')     #string
print(type(x),)  
x1=('Talha',)   #tuples
print(type(x1))

# using double paranthesis in tuples as shown below:
my=(('Talha','Islamabad','G9 resident')) 
print(my)
print(type(my))

#   accessing the elements -> First is indexing
print(friends[3],numbers[0])
#   the negaticve indexing is same
print(Boolea[-2])
#   the indexing can be limited between some indexes
print(friends[2:5])   #simple
#   printing the values before the indexed
print(numbers[:5])
#   printing the values after the indexed
print(friends[4:]) 
#   printing the negetively indexed elements of the tuple under study
print('\n',friends[-4:-1])   # ok  
print('\n',numbers[:-1],numbers[-1:]) # done

#checking for the presence of an element
if 'Husnain' in friends:
    print(True)


#   UPDATING THE ELEMENTS OF THE TUPLE
# note that the tuple is immutable, so we convert the tuple into list
y= list(fruits)
y[1]="peach"
fruits=tuple(y)   #not commutative 
print(fruits)   

#   using the append method
y1=list(friends)
y1.append('Muneeza')    # simply added in the end
friends=tuple(y1)
print(friends)

#   Adding multiple tuples
friends +=fruits
print(friends)         # simply + add

#       note that the tuples are immuteable, so we can't remove items
#       similarly convert the tuples into the list
y2=list(friends)
y2.remove("Ahmed")
friends=tuple(y2)
print(friends)

del numbers
#print(numbers)          # would raise errors cuz the tuple has been deleted

#   unpacking and packing in tuples:
#   ->unpacking similar to indecing :prints the value as indexed, thus the size should be same as the orginal tuples
(green,yellow,red,purple) =fruits
print(green)
print(yellow)
print(red)
print(purple)  # simply changes

#   applying Asteric, does following:
#       ->  The number of elements in the brakcets should be equal to the number of elements in the tuples
#       -> if we don't want to have same number of elements in both, we would use asteric *
#       -> can be seen as following:

(a,b,c,*d) =friends
print('\n',a,'\n')
print('\n',b,'\n')
print('\n',c,'\n')
print('\n',d,'\n')  # rest in the friends tuple
(q,*w,e) =Boolea
print('\n',q,'\n')
print('\n',w,'\n')   # similar reason
print('\n',e,'\n')

for x in friends:
    print(x)   # simple
print(' ')
for x in range(len(friends)):
    print(friends[x])
print(' ')
i=0
while i <len(fruits):     # similar 
    print(fruits[i])
    i=i+1
print(" ")


#   joining the tuples:
newtuples = Boolea + cars
print(newtuples)

#       multiplying the tuple's elemnts with any integer to print number of times you want to print elements in the final tuple
newtuple1= cars *3
print(newtuple1)   # simple 

#           methods in the tuples:
print(cars.count('BMW'))
w =cars.index("honda")   # tells the index of the element in the list
print(w)

y1='talha','honda','city',2007
print(type(y1))  # tuple

A =(1,1,1,1,2,3,4,5,6,7,8)
A1 =A.index(2)
print(A1)