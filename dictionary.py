print("Talha =>")

# note in python 3.7, the dictionary is ordered but before that the dictionary used to be unordered.
#another important thing to remeber is that we an add list in the dictionary
# mutable 
bio={
    'name':'talha',
    'dep':'electronics',
    'Institute':'QAU',
    'city':'Islamabad',
    'DOB':2002
}
hyundai ={'sonata','santor','Starex','Tucson','Elacntra'}
friends={
    1:"talha",
    2:"kashif",
    3:"Sohaib",
    4:"Hamzee",
    5:"Daniyal",
    6:"rana",
    7:"Hassan",
    8:"HUsnain",
    9:"Ahmed",
}
print(bio,"\n",friends)
print(" ")
print(bio['city'])    # city is a key of the dictionary        => done

#               DICTIONARY CAN'T HAVE TWO KEYS THAT ARE SAME I.E REPITION
mustang={'brand':'ford','model':1965,'model':'sedan','color':'red'}     # IN THIS CASE WE ONLY GET THE ACCESS OF LATER COMING KEY BUT IF KEY AND THE COMMENT ARE SAME:
mustang1={'brand':'ford','model':1965,'model':'sedan','color':'red','color':'red'}   # printed once 
print(mustang)
print(mustang1)

# passing list in the dictionary
mustang2={'brand':'ford',
           'model':1965,
           'model':'sedan',
           'color':['red','white','blue']
}
print(mustang2)       #got it

#                   ACCESSING THE ITEMS FROM THE DICTIONARY
# easiest way:
print(friends[6])
# can also be done with get function:-
y =mustang.get('model')
print(y)

#   if we only want to acces the keys of the understudy dictionary, we use key()
y1 =friends.keys()
print(y1)             #SIMPLE 



friends[10] ="Maeeda"
print('\n',friends,'\n')            #simple addition

# similarly if we want to print the values of the dictionary, we use the values()
y2 =mustang1.values()
print(y2,'\n')                  # simple as dog


#               simple mutable:
mustang2['model'] ='hatchback'  # simple addition in the existing dictionary
print(mustang2)

#           items being printed in the given dictionary
y3 =friends.items()
print(y3)       #divide all the elements in small tuples

# checking for the presence of anything in the dictionary using if statement
if 'Institute' in bio:          #Note that the if statement only finds the element ion the key
    print("Yes! IT IS HERE")

# changing can be done by update() method  and other can be simple 
bio['Father name'] ="Zahid Naseem"
print(bio)

bio.update({'CGPA':3.5})
print('\n',bio)


# removing elements from the dictionary
#                           =>pop()
#                           =>popitem()-> removes the whole item but the last one
#                           =>del funtion ->with the same error after deleting 
mustang2.pop("brand")
print('\n',mustang2,"\n")

friends.popitem()
print(friends)

del mustang1['model']   #takes only one argument 
print('\n',mustang1,"\n")
#   can also delete the whole dictionary

"""del mustang
print(mustang)        #error """


mustang1.clear()
print(mustang1)             # simple clear

#       loops in the dictionary
for x in bio:
    print(x)   
print(' ')
for x in bio.keys():
    print(x)
print(' ')
for x in bio.values():
    print(x)                    # SIMPLE 

#               printing the dictionary as it is
for x,y in bio.items():     # we want to print the whole item
    print(x,y)
print(" ")
for x,y in friends.items():
    print(x,y)


#           copy elements   copy()
mydict= friends.copy()
print(mydict)
print(' ')
(mydictionary)=dict (friends)
print(mydictionary)
print('\n,','\n')
disc =dict(bio)
print(disc)

#               nested dictionaries 
myfamily ={ 
    "child1":{
        "Name":"Talha",
        "DOB":"16/04/2002"
    },
     "Child2":{
         "Name":"Momina",
         "DOB":"5/8/2004",
     },
     "Child3":{
        "Name":"Taha",
        "DOB":"27/9/2007",
     }
}
print('\n',myfamily,'\n')

p1={
    "car":"mercedes",
    "model":1980
}
p2={
    "car":"porchea",
    "model":1965
}
p3={
    "car":"Toyota",
    "model":2022
}
mycars={
    "car1":p1,
    "car2":p2,
    "car3":p3
}
print(mycars)      #DONE
print(' ')
prctice ={
    "1st dictionary":mustang,
    "2nd dictionary":friends,
    "3rd dictionary":bio
}
print(prctice)

garee={
    "car1":{
        "name":"landcruiser",
        "color":"White"
    },
    "car2":{
        "name":"Audi",
        "color":"Black"
    },
    "car3":{
        "name":"BMW",
        "color":"Silver"
    }
}
print(' ')
print(garee)

#                   METHODS  => CLEAR()
#                            =>copy()
#                            =>fromkey()
mycars.clear()
print('\n',mycars,'\n')

dic =friends.copy()
print(dic)

X ={'thinkpad','lenovo','T430'}
ya=0
for x in X:             #simple
    newdictionary =dict.fromkeys(X,ya)
    print(newdictionary)

#####             syntaxe =>dict.fromkey(key,value)
p='forte'
newz =dict.fromkeys(hyundai,p)
print(newz)

#           get() -> simly print the valaue of any key
Y =friends.get(2)
print(Y)
#                   -> if we want to print the value that is not in the original dictionary
V =bio.get('depart','Cs') # enter new key and value then print it  
print(V)

v =bio.setdefault('dep','COmputer science')    #original value is printed 
print(v)
print("         ")
print("         ")
print("         ")
print("         ")
print("         ")


from pprint import pprint
no = dict(x=list(range(11, 20)), y=list(range(21, 30)))
pprint(no)
print(no["x"][4])
print(no["y"][4])
#print(no["z"][4])
for k,v in no.items():
   print(k, "has value", v)