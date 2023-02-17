print(" FOR LOOP    ")

# in a list 
friends=['Talha','Google','Microsoft','IBM']
for x in friends:
    print('\n',x)
for x in 'GOOGLE':
    print(x)

fruits=list(('Apple','Mango','orange','pinus','Banana'))

for x in fruits:
    print(x)
    if x == 'orange':
        break
print(" ")
for x in fruits:
    if x == 'Mango':
        break
    print(x)

# if we want to remove one element -> continue
print(" ")
for x in friends:
    if x=="Microsoft":
        continue
    print(x)


for x in "friends":
    print(x)


for y in range(6):
    print(y)

#           WHILE USING START AND STOP PARAMETER
print(" ")
for y in range(2, 10):
    print(y)

print(" ")
#               WE CAN SPECIFY THE INCREAMENT VALUE OF EACH PARAMETER IN A LOOP 
for y in range(2,15, 2):                # specifying the difference of 2(even multiples)
    print(y)

#           WE CAN USE THE ELSE STATEMENT 
print(" ")

for z in range(13,16, 2):
    print(z)
else:
    ("print not in the loop ")          #out of the loop doesn't print why ???

print(" ")
for a in range(17):
    if a==11 : break
    print(a)

else:            
    print(" OUT OF LOOP ")         # note that in this case the if loop is broken and the else statement is not executed


print(" ")
#               NESTED LOOPS // FOR LOOPS 
games=list(('hockey','badminton','cricket','football'))
companies=list(('GOOGLE','LENOVO','MICROSOFT'))
for x in games:
    for y in companies:
        print(x , y)     #Note that the list is prited the number elements in the list are present 

# the same use of pass function -> to reduce the error in the code 
for x in ['apple','mango','orange']:
    pass       # no error
