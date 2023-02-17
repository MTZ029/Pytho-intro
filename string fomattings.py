print(" THE STRING FORMATTING METHODS   ")

x =input('  PLEASE ENTER THE LAST TWO DIGITS OF YOUR REGISTRRATION NUMBER ')
y =" The entered registration number is {}"
print(y.format(x))   # the value is simple and easy

# we can limit the printing element to two decical points
price = 450
z ="    THE REGISTRATION NUMBER IS {:.2f}    "
print(z.format(price))

# multple different functions are possible in the string

z1 =" The name is {},the departmetn is {},the registation number is {:.2f}, the number of vehicles in the grade are {:.50f}"
z2 ="Muhammad Talha Zahid"
z3 ="Electronics"
z4 =4102013029
z5 =2
print(z1.format(z2 ,z3 ,z4 ,z5))

# we can also let the indexed string to printed as shown below :
print('     ')
a2 = "Talha"
a3 ="Germany"
a4 ="20"
a1 ="the name is {0}, the country is {1} and the phone number is {2:.2}"
print(a1.format(a2 ,a3 ,a4))

print("             ")
# the indexing can change
s ="the name is {1},{1} is {0} years old "
s1 ="Muhammad Talha Zahid "
s2 = 20
print(s.format(s2 ,s1))    # s2 is 0 indexed , s1 is 1 indexed
 
print("     ")
q ="the vehicle is {car}, and model is {year}"
print(q.format(car ="honda",year =2007))