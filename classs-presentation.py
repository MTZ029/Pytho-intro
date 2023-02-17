a="talha zahid reporting from CALTEC institute of sciences \n"

print(a)


print(a.capitalize())

print(a.casefold())

print(a.center(500, 'n'))



a="My name is {fname}, I am {age} years old, and I ride {name}".format(fname="Talha",age=20,name="motorbike")
print(a)
a2="My name is {0}, I am {1} years old, and I ride {2}".format("Talha",20,"motorbike")
print("\n",a2)
a3="My name is {}, I am {} years old, and I ride {}".format("Talha",20,"motorbike")
print("\n",a3)

a45="the price of patrol today is {:.12f}"
print(a45.format(230))


a7="Q\tA\tU"
print(a7.expandtabs(23))

coutries=['pak','Aus','Ind','Eng','S.A','Iran','Afg','Kzghst']
empytlist=[]
zerolist=[]

for x in coutries:
    if 'g' in x:
        empytlist.append(x) # append means add, thus the program itself adds the index for the elemnts with g in it 
print(empytlist)

# simply practicing with while loop:
'''y=0
while y<len(coutries):
    if 'g' in y:        -> simply when we are concerned about the presence of elements that is for x in y, while loop fails to operate
        zerolist.append(y)
print(zerolist) '''

xoxo=[i for i in coutries if 's' in i ]
print(xoxo)

LIST=[x for x in coutries if x !='Afg']
print(LIST)

newlist=[x if x !='Aus' else 'Russia' for x in coutries]
print(newlist)

newlist2=[ x if x !='pak' else 'Israerl' for x in coutries]
print('\n',newlist2)

#n=[x if x !=;'pa' else 'is' for x in countries]
z=[1,23,3,4,4,5,45,45,45,453,53,5,34,4,53,5,35,453,5,6,3262,62,63,44,4,4234,3]
for g in z:
    coutries.append(g)
print(coutries)

def duntion(x):
    return abs(x - 90)
z.sort(key=duntion)
print(z)


