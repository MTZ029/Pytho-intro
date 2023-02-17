print("Presentaion")

bio ={
    "name":"talha",
    "dep":"elec",
    "reg":29
}

car={
    "name":"civic",
    "mocel":2022,
    "color":"red",
    "color":"blue"
}

print(bio,"\n",car)

print(bio["dep"])

y =bio.get("name")
print(y)

# syntax dic ={key :value }
print(" ")

y1 =car.keys()
print(y1)

y2 =car.values()
print(y2)

car["make"]="Japan"
print("\n",car)

# if an element exists in the dictionary

if "name" in bio:
    print(True)
else:
    print(False)

# update()

bio.update({"Gpa":3.5})
print(bio)

# remove ->pop()
bio.pop("dep")  
print(bio)

car.popitem()
print("\n",car)

"""
del car
print(car)"""

del car['mocel']
print(car)

car.clear()
print(car)

print(" ")
# loops printing
for x in bio:
    print(x)

for x,y in bio.items():
    print(x , y)

for y in bio.values():
    print(y)

for x in bio.keys():
    print(x)

# copy()

a =bio.copy()
print('\n',a)

"""
x = dict("name":"t",2:"s",3:"z")
print(x) """

children ={
    "child1":{
        "name ":"x",
        "age":20
    },
    "child2":{
        "name":"y",
        "age":19
    }
}

print(children["child1"])

p1 ={
    "one":"H",
    "age":22
}
p2={
    "two":"J",
    "age":24
}
P ={
    "A":p1,
    "B":p2
}
print(P)

x ={"A","b","C"}  # set
p=int(input("enter the value"))
for y in x:
    new =dict.fromkeys(x , p)
    print(new)


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x =int(input("Enter the key"))
if x in d:
      print('Key is present in the dictionary')
else:
      print('Key is not present in the dictionary')

# we can only acces the dictionary from keys