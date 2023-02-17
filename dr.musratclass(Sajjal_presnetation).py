print("simple dictionary")


bio={
    "name":"Talha",
    "Inst":"QAU",
    "City":"Islamabad ",
    "Reg.no":29
}

friends ={
    1:"talha",
    2:"Kashif",
    3:"Sohaib",
    4:"Hasssan",
    5:"Hamzee",
    6:"Ahmed",
    7:"Daniyal",
    8:"Rana",
    9:"Husnain"
}
bio1={
    'name':'talha',
    'dep':'electronics',
    'Institute':'QAU',
    'city':'Islamabad',
    'DOB':2002
}
print(bio)
# acces only one item
print(' ')
print(bio["Inst"])
print('  ')
bio["name"]="Kashif"
print(bio)

car={
    "name":"city",
    "model":2007,
    "model":2008,   # later coming value of the same key is printed always
    "make":"japan"
}

print('\n',car)

c =car.get("model")
print('\n',c)   # printeed our model

# we can also access the keys only 

x =bio.keys()
print('\n',x)
print(" ")
y =bio.values()
print(y)

car["model"]="sedan"
print("\n",car)

y1 =car.items()
print("\n",y1)

if "name" in car:
    print("Indeed the name is there")
else:
    print("No ")

car["color"]="blue"

print("\n",car)   # simply add 
#addiiton method update()

bio.update({"CGPA":3.5})    # simple update method 
print("\n",bio)

#      => removing element:

car.pop("name")
print("\n",car)    # name is removed 

# pop item removes all the irems from the dictionary understudy

car.popitem()
print("\n",car)

car.popitem()
print("\n",car)

car.popitem()
print("\n",car)

del bio["City"]
print("\n",bio)

bio.clear()
print("\n",bio)

print(" ")
for y in friends:
    print(y)    #simplpy prints the keys 

print(" ")
for x in friends.values():
    print(x)

print(" ")
for x,y in friends.items():
    print(x,y)


fr =friends.copy()
print(fr)

b =dict(bio1)
print(" ")
print(b)

o=0
for x in bio1:
    new =dict.fromkeys(bio1,o)
    o= o+1
    print(new)

t =bio1.get(2)
print(t)



p =bio1.setdefault("dep","IT")
print(p)



s2=dir(bio1)
print(s2)
for x in s2:
    print(x)

print(" ")

from pprint import pprint
pprint(s2)


name1 ={
    "name":"talha",
    "age":20
}
name2={
    "name":"sohiab",
    "age":20
}
name3={
    "name":"Ali",
    "age":19
}

intor ={
    "boy1":name1,
    "boy2":name2,
    "boy3":name3
}

intor2={
    "name":{
        "name":"talha",
        "age":20
    },
    "name5":{
         "name":"taha",
         "age":20
        },
    "name9":{
        "name":"maeeda",
        "age":20
}
    }
print( "    ")
print(intor2)

print(intor)