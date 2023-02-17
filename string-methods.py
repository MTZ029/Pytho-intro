
txt= """name talha Zahid
      department electronics
      registration 04102013029
      RESIDENT ISLAMABAD
      Blood group B+
      Father name zahid Naseem
      Societies  tMS, sPIE , eSS\n"""
w=(" ")
w1="My NameIsTalhaAndIAmPro"
w2="Talha , Rana , Sohaib , Hamzee , Ahmed , Husnain , Mian Hassan , Kashif"
w3="                     is               "
w4="....................################# helo *************&&&&&&&&&&&&"

tx="hello WOLD THIS THE TALHA FROM ISLAMABAD and is here for machine learning\n"
# for encode (special character)
j="T@lha Zȧhid"
polo="pakistan"#   is working for me"
s="I\tL\tO\tV\tE\tY\tO\tU"
digi="1234567890"
xx="help? !@ need help ?"
#                       Print
print(txt)
print(tx)

#             Checking for the capitalization   -> just used to capitalize the first element
p=tx.capitalize()
print(p)
print(txt.capitalize())

#               casefold() -> used to lowercase all the elements of the string
print(txt.casefold())
print(tx.casefold())

#               center() -> This is helpful when the string is smaller than the size we recquire it to  be
#                        ->Padding is another process in this scenari in which the alpabet padded is used in the place of empty-spaces.
print(txt.center(1500,'T')) # I want to print t in the plac eof empty spaces.
print(tx.center(120 , 'X'))

#               cout()-> used to count a number, alphabet or even a word but not the total number of alphabets i the string.  
ct=txt.count("e")
ct1=tx.count("W")
print(ct)
print(ct1)

#               encode() -> encodes the string into bytes and ascii when recqired.
#                        -> most efficient way of storing th estring 
#                        -> special character are dealt accordingly 
#                        -> special characters are ignored or replaced while using ascii
print("\n")
O=tx.encode()
#encoding can do the foullowing:
u=j.encode('ascii','ignore')  #it ignores the special character bveing used
u1=j.encode('ascii','replace') #it replaces the sepcial charactern being used.
u2=j.encode('ascii','backslashreplace')  # replaced by back slash
u3=j.encode('ascii','namereplace') #literally tells about the special character -> a with ring above it
u4=j.encode('ascii','xmlcharrefreplace') # prints as it is
print(P)        #UTS-8 / in the form of bytes if nothing in the comment section of the encode()               
print("\n")
print(O)
print("\n")
print(u)
print(u1)
print(u2)
print(u3)
print(u4)

#               endswith() -> uses boolean to return the point, the answer is true or false.
q1=txt.endswith("eSS")
q2=tx.endswith('learning')
q3=j.endswith("d")
print(q1,q2,q3)
print("\n")

#               expandtabs() -> used to manipulate with the strings using tabs in them, we can print the answer with the desired spaces using this function.
print(s)
a1=s.expandtabs(20)
a2=s.expandtabs(200)
a3=s.expandtabs(2000)
print(a1)
print(a2)
print(a3)
print("\n")

#           find() _> finds the alohabet or data from the stirng if not found it  return -1
print(txt.find('talha'),"is the value")
print(tx.find("a"))
print(j.find("1"))

#         format()   -> used to make the format for any buying, selling or nama fill etc,
print("\n")
txt1="today's sugar prices is {price:.20f} Ruppees"  #this specifies the precision of 100
print(txt1.capitalize())
print(txt1.format(price = 100))

txt2="/n The name of this department is {fname}, and a student for {age} years"
print(txt2.format(fname="electronics",age=2))
a="My name is {fname}, I am {age} years old, and I ride {name}".format(fname="Talha",age=20,name="motorbike")
print(a)
a2="My name is {0}, I am {1} years old, and I ride {2}".format("Talha",20,"motorbike")
print("\n",a2)
a3="My name is {}, I am {} years old, and I ride {}".format("Talha",20,"motorbike")
print("\n",a3)

txt107 = "We have {:<12} chickens."
print(txt107.format(49))
txt2 = "we are {:>12} humans."
print(txt2.format(16))
txt3="we have {:=12} marks,"
print(txt3.format(19)) # placed the sign to the left postion like above code
txt4="we love {:^17} dishes."
print(txt4.format(170))
txt5="Ali is imporved from {:+} to {:+}"
print(txt5.format(-45,50))
txt6="Kashif has improved from {:-} to {:-}"
print(txt6.format( - 48 , 80))
txt7="My earning would be InshaAllah {:,}"
print(txt7.format( 25000000))
txt8="My registration number is {:_}"
print(txt8.format( 4102013029))
txt9="The binary value of {0} is {0:b}"
print(txt9.format( 11 ))
txt10=" The unary code of {0} is {0:c}"
print(txt10.format(101 ))
txt11=" There are {:d} homes in my town "
print(txt11.format(0b0110))
txt12="we have {:e} dimenesions in the complex planes and can also be done with captial E as {:E}".format(122,90)
print(txt12)


x13=float("nan")
x4=" tha name is {:F}"
print(x4.format(x13))
x9=" we are {:f}"
print(x9.format(x13))   # inf and nan

txt14="the value of {0}  in octal is {0:o}"
print(txt14.format(155))

txt15="the value of {0} in hexa is {0:x}"
print(txt15.format(155))

txt15="the value of {0} in hexa is {0:X}"
print(txt15.format(155))

txt16="Your percentage is {:%}"
print(txt16.format(0.75))

txt17="Your percentage is {:.0%}"   #without decimal points
print(txt17.format(0.75))


# fomrat_map() -> the input is taken from the dictionary and no need to take input from the format method
print("\n")
o1="My name is {name} and my department is {dep} and I am a student of {uni} and my registration is {reg}"
dick={'name':'talha','dep':'electronics','uni':'QAU','reg':'04102013029'}
print(o1.format_map(dick))
#print(o1)




#           index()- > the indexing
z2=tx.index("e"),j.index("T")
print(z2)


#       isalnum() -> the method is used for checking for the alphanumeric prsence in the string being used.
u12=tx.isalnum(),j.isalnum(),polo.isalnum()
print(u12) # note that in isalnum , the boolean is true only when we are given with only one alphabet in string

#   isalpha -> used to check for the alphabet
y5=txt.isalpha(),polo.isalpha()
print(y5)

#       isascii -> this checks that if the ascii value exists or not
z14=txt.isascii(),j.isascii()
print(z14) #The ascii exists or not 

#       isdecimal() -> checks for the decimal prsence in the nstrin being used 
z18=tx.isdecimal()
print(z18)

#      isdigit( ) -> is used to chek foir th edigit presence in the string being checked
print(txt.isdigit(),tx.isdigit(),j.isdigit(),polo.isdigit(),digi.isdigit())   #none of these are in the form  of digit except digi

#     isidentifier()   ->checks for the valid identifier.
print(txt.isidentifier(),tx.isidentifier(),digi.isidentifier()) # make sure that ther shouldn't be any spaces in the string being used

#     islower()   -> used t0 ache check for lower case alphabets in a string
print(tx.islower(),polo.islower())

#     isnumeric() -> is used to check numeric values of string
print(tx.isnumeric(),digi.isnumeric())

#     isprintable()   -> check weathjer the string bein used is printable !
print(j.isprintable(),txt.isprintable(),polo.isprintable(),xx.isprintable())

#     isspace()   -> check for spaces in the string
print(w.isspace(),txt.isspace())

#     istitle()   -> checks for the rules of tile followed or not !
print(w1.istitle(),txt.istitle())

#     isupper()      -> if all the alphabets are upper case.
print(txt.isupper(),polo.isupper())

#     join()  -> is used to join the spaces and fill in the balnk space.
zp="o".join(txt)
#print(zp,"\n",'talha'.join(t x))

#     ljust()    ->  used to print something on the right side of the string already stored
h=j.ljust(15)
print(h,'talha is the best')   # would be printed after 15 spaces
b='banana'
bA=(b.ljust(100))
print('out of all fruits',bA,'is my favourite')
hg=j.ljust(20,'e')
print(hg,'pakistan is worst')

#     lower()     ->convert all the characters in the string in lower keys
print(txt.lower(),polo.lower(),j.lower())





#                 Dr Musarat

#     translate()   to ask from sir







#     maketranss()  ->change the alphabtes in the selected stirng
cha=w1.maketrans("m","P")
print("\n",w1.translate(cha))
st001="my sex is male"
e=st001.maketrans('e','r')
print(st001.translate(e))
#      can also be done with multiple strings
#      note that the if we have 3 strings, the third is given to none 
f="bye bye birdy"
f1="xyz"
f2="abc"
f3="qwe"
mytabs=f.maketrans(f1,f2,f3)
print('\n',f1.translate(mytabs))      # -> ASK SIR MUSARAT

#     partition()       ->divides the string in multple tuples as shown in the code below:
print(txt.partition('department'))
print('\n',w1.partition('Talha'))   #understood
#note that if the asked partition is not in the string we are working with ,it would print empty like this (..,..)
print('\n',tx.partition('welcome')) #done

#     replace()   -> used as maketrans() but easier, the code is here to show how it works
l0="one the one was one in the one and two was two in the two for two too"
print(w1.replace('Name','Noun'))
print(l0.replace('one','none',2)) # note that the two inputs are always string max 3 inputs arguments in replace()

#     rfind() ->  note that this would work similar to index()
print(l0.rfind('one')) #understood
xa=l0.rfind('one',0 , 3)  # it limits the search are from the index 4 to 9
print(xa)
print(l0.rfind('t'))    # the last t occurs here
print(l0.index('t'))    # the first t occurs here

#     rindex()    ->note that the first value would be printed here
print(l0.index('and'))
#print(l0.index('t',5,13))  note that the limitng factor wourld not work in this scenario
print(l0.index('t'))

#     rjust() ->smae as ijust() but the values printed on the left
print(w1.rjust(200,'m'))     # no spaces allowed
 # note that if we want to print some sentence along it, the way is :
lk="talhaisthestudentofelectronics"
lk1=lk.rjust(400)
print('\n',lk1,'electronics is tough')

#     rpartition()      -> same as partition divides into muktiple tuples same as partition 
print(txt.rpartition('name'))
print(w1.rpartition('o')) #takes only one argument

#     rsplit()    -> use to convert the string into list 
print(txt.rsplit(','))
print('\n',j.rsplit(','))                 # note that the string with commas only work in this scenario
print('\n',w2.rsplit(','))   # have no idea what does the integer along it does to it

#     splitline() -> used to split the string from were we have place \n.
#                  -> another point to notice is that when we pass the argument of true in the splitline(true), the '\n' is printed itself in the final answer
print(txt.splitlines())
print('\n',w1.splitlines()) # the major differnece between split and splitline is that it doesn't necassarily need commas in the string .
print('\n',w1.splitlines(True))  # note that if true is written, the \n is present in the partitions

#     startswith()      -.same as endswih()
print(w1.startswith('My'))    
print(w2.startswith('Rana',8,13))  # the value is true

#     strip()     -> used to remove the spaces of the string and joins the strings together
#oh=w3.strip()str102=str100.__add__(str101)
#print("department of electronics",oh,"the part of NIE")   # printed perfectly
#     when we want to remove or ignore something from the string in the final answer, pass it in the comments for the strip()
ohh=w4.strip('.#&*')
print("when I am alone",ohh,"loops") #only works for the no space strings

#     swapcase()  -> changes the uppercase to lower case and lower case to upper 
print(w1.swapcase())

#     title()     ->capitalises all the words in the given sring
print(txt.title()) # THING to remember is that the alphabet capitalises after the integer

#     upper()     -> simply capitalize all the elements of the string
print('\n',txt.upper())

#     zfill()     -> fills the text with 0 insted of empty spaces
print(w3.zfill(120)) # printed zero

x=["Talha","sohaib","kashif"]
print(x.append('Mian'))     # what's wrong ?

str100="Talha is a student"
str101=" he is a student"
str302=str100.__add__(str101)
print(str302)
 
 #print(len(txt))

 
P=txt.encode('ascii')
print(P) 
print(ord(j))