print("Talha Zahid")
L=['talha','Pakistani','Islamabadian','G9 resident','student','major in electronics','Qaidian']
L1=['suzuki','toyota','honda','changhan','BMW','mercedes','Pontiac','Rollsroyace','BMW'] # Allows reptition
L2=[12,12,21,21,121,13,14,41,220]
L3=[True,False,False,False,True]
k=['Hassan','Kashif','Talha','Rana','Ahmed','Sohaib','Husnian','Humzee','Daniyal']
A=["Barkahu","G9","DHA","F7"]
print(L)
print('\n',L1,'\n',L2,'\n',L3)

# lenght
print(' ')
print(len(L))

# we can use the list constructor to make the list as shown belloW:

L4=list(('pak','Ind','Iran',1,'Afg',True))  
print(type(L4)) # List

# Access the list items:
print(L4[1],L1[2:5])  #between the listed indexes
print(L[:4]) # print all except this index
print(L[2:]) #neglects the elements before it 
print("\n",L[-3:-1]) # note that in negative index, the index can't be used as [-1:2]

#checking for the existance of an alphabet in the given lsit
if 'Islamabadian' in L:
    print('yes it exists')

# overwriting the elements of the LIST
L[0]='Hassan'
print(L)
# intechanging of values
L[2:3]=['Sialkotian','Sialkot residen']
print(L)



         # ASK 

# replacing multiple value at once 
L2[2:3]=['HYUNDAI']
print("\n",L2)        #what's wrong with that ?


#    inserting elements in the list 
L2.insert(0,'Talha Zahid ') #location specifier
print(L2)   # print saperately 


#   extending the already existing list or you can say that we want to add two lists
L.extend(L1)
print('\n',L) 
L.append(L1)  # not list within a list so! means [....[...]] but as a single list so differnce between append and extend
print('\n',L)
L4.extend(L3)   
print('\n',L4)
L4.append('Secret')
print('\n',L4)

#   removing elemets from the list 
#remove()
L1.remove('honda')  # simple removed the alphabet from the list 
print(L1)

#   pop()   -> or simply remove 
L4.pop(1)
print('\n',L4)             #simply pops out the idexed element from the list
print(L2.pop())           #Prints the last element only
print(L2)                   #print all elements except the last 

# del fubction 
#   -> removes all the elements from the list as del obj
#   ->removes indexed element from the list del obje[0]
#del k[7]
print(k)
#del k
#print (k) # as delted no would give error 

# clear list -> clear()
 #k.clear()
 #print(k)  # cleared out the elemts from the list thus we have the empty list printed 


# Loops # -> simply printing the elements of the list
print("\n")

for i in L2:
    print(i)
    for x in k:
        print(x)

# using the loops by using the range in the system

print('\n')
for j in range(len(L1)):    # lenght is defined automatically by the lenght of the list being used
    print(L1[j])

for x1 in range(len(L2)):
    print(L2[x1])

#   while loop is solved here
fruits=['mango','apple','orange','appricote','plum','leechee','peach']
# the h is initialised saperately
h=0
while h<len(fruits):
    print(fruits[h]) #Simply passing the indexes through the existing list
    h=h+1   # simply adding thje indexes 

print(' ')
h2=0 # initial indexing
while h2<len(k):
    print(k[h2])
    h2=h2+1

#            short Hand for looooops 
[print(x2) for x2 in fruits]    #-> this is called list comprehension

print(' ')
[print(f) for f in L1]    # simply the short form of loops


# simply check for the presence of an alphabte and if it exists, print the whole world
newlist=[]

for xx in fruits:
    if 'c' in xx:
        newlist.append(xx)
print(newlist)  # working poerfectly


# using the short habnd 
zzz=[c for c in fruits if 'e' in c]
print(zzz)

# ! this mark is used to say print all except this
d=[c2 for c2 in fruits if c2 != "peach"]     #true for all elements except peach
print(d)

s=[t for t in range(100)]    #simply the list would be given  form 0 to 99
print(s)
#   SIMPLY APLLYING THE LIMIT 
s1=[y for y in range( 1000 ) if y>100] 
print(s1)
print(' ')

s2=[a.upper() for a in fruits]    # SIMPLE THE UPPER 
s3=[b.lower() for b in k]
print(s2,'\n',s3)
#   set all the values to anything in the string
newlist1=[True for x in k]
print(newlist1)
# replacing the elements as can't do as simply done in string
newlist2=[x if x !='peach' else 'guava' for x in fruits]
print(newlist2)
print(' ')
z=["lenovo","dell","hp","samsung","allienware","toshiba","z","panasonic","skyworth","tCL"]
k2=[100,92,1,23,2,44,14,166,12,323,22,4,1]

#                   DATA SORTING    
#                   -> alphabatically
z.sort( )
print(z)      # note that we need to use doube conotation marks for the process of sorting
A.sort()
print(A)

k2.sort(reverse=True)    #decsending order
print(k2)

def talha(x):
    return abs(x - 10 )
k2.sort(key=talha)   # value nearest to 10
print(k2)

fruits.sort(key=str.lower)
print(fruits)     # descending order->    from a to z

z.reverse()    # reverse from z to a
print('\n',z)


#           COPY LIST 
newlist3=A.copy()       # simple copy
print('\n',newlist3)

newlist4=list(k)    #simple copy
print(newlist4)


e=['Talha','Sohaib','Hassan']
f=['Google','IBM','MetaVerse']
g=e+f
print(g)

print(' ')
for x in f:
    e.append(x)
print(e)


w=[1,2,3]
q=[4,5,6,4,4,4,4]

q.extend(w)
print(q)
#   ANOTHER METHOD IS 
for j in q:
    w.append(j)
print(w)

L.append('somefome')
print(L)


L.append(e)    #brackets walaa issue
print('\n',L)

#           -> count()
print(w.count(4))     #atleast one argument needed

print(e.count('Sohaib'))

