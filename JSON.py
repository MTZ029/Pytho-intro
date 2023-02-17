import json
# JSON  -> JAVA SCIPT OBJECT NOTATION   // USED FOR THE EXCHANEGE OF DATA
print('THIS IS THE ORIGINAL POGRAM FOR THE JSON LIBERARY    ')

# simply you can say the copying of the original data 



# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

a ='{"name":"Talha","age":20,"city":"Islamabad"}'

b =json.loads( a )
print(b)     # simple as copyinf of dictionary into another 


#    the printing and converting of pyhton to json

x1 ={
    'name':'Muhammad Talha Zahid',
    'job':'Microsoft',
    'country':'America',
    'state':'baltimore',
    'income/month':100000,
    'Father Name':'Zahid Naseem'
}

x2 =json.dumps( x1 )
print(' ')
print(x2)

# we can convert the pyhton of the objects of the following types:
''' dict
list
tuple
string
int
float
True
False
None '''
print(' ')
print( json.dumps({'name':'Talha','department':'Electronics','Reg number':'04102013029','resident':'america'}))
print( json.dumps(['Talha','Sohaib','Ahmed','Hamzee','Daniyal','Kashif','Husnain','Hassan','Rana']))
print( json.dumps(('hyundai','Kia','Pegeut','Mercedes','Volkswagon','BMW','Audi')))
print( json.dumps(('House number 36 street number 6A ')))
print( json.dumps(24.15))
print( json.dumps(24))
print( json.dumps(True))
print( json.dumps(False))
print( json.dumps(None))

print(' ')

bio ={
    "name":"Muhammad Talha Zahid",
    "age":20,
    "married":False,
    "Divorsed":False,
    "Children":None,
    "Pets":('dogs,','Parrots'),
    "cars": [
        {"model":"Rolls Royace","Model":2022,"mpg":29.2},
        {"model":"BMW","Model":1965,"mpg":19.5}
    ]
}
x11 = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(bio))
print(' ')

# index can also be written in order to print a specific value for the bio dictionary

print( json.dumps(bio , indent= 2))   # indent is the spacing of the printed values

print(' ')
# sapartors => can also be written
print( json.dumps(bio , indent=3 ,separators=(",","=")))   # the 1st , is use in the end of every sentence and = is use in the place of :
print(' ')
print(json.dumps(x11,indent =4,separators=(",","#"),sort_keys=True))     # this is simple 

# prictice on text file 1