print(" ENVOKING THE REGULAR EXPRESSION ")
import re    #reular expression
intro ="THE NAME IS MUHAMMAD TALHA ZAHID AND I AM STUDENT OF NATURAL SCIENCES AT QAU ISLAMABAD, FURTHERMORE AM PASSIONATE ABOUT THE MACHINE LEARNING PART OF THE STUDY   "
in1 =" the value that comes from the sum of 2 +2 is always 4"
intro1 =re.search("the.STUDY",intro)    #checking for 'the' as the starting alphabet of stirng and 'study' as the last word in the string under study
if intro1 :
    print(' YES INDEEED ITS TRUE    ')
else:
    print(' NOT IN THE STRING   ')    # even if oe of the is true!!!! Ture is printed

intro3 =re.findall("IS",intro)
print(' ')
print(intro3)    # simple!
intro4 =re.findall("Pakistan",intro)
print(intro4)    # prints the empty list 

x ="My name is Talha and I am a student at QAU and living here for 19 years"
x1 =re.search('\s',x)  # white space
print('the white spaces are ',x1.start())

print(' ')
x2 =re.search("ZAHID",intro)
print(x2)       #match is placed in the output Other wise none is printed

x3 =re.split("\s",intro)    # can be done \s,\t,\n  => check for the printed string all are different from one-another
print(' ')
print(x3)

# WE CAN CHECK OR LIMIT THE NUMBER OF TIMES WE WANT THE SPLIT FUNCTION TO WORK ON DIFFERNT INDEXES

x5 =re.split('\s',intro,5)     #working for the 5 indexes
print(x5)

print(' ')
x6 = re.search("ME",intro)
print(x6)
#    SUBSTITUTING THE THE SPACES OR ANYHTING WITH ANY ALPHJABET OR ELEMETN WE WANT TO 
print(' ')
x7 =re.sub("\s","4",intro)
print(x7)    # simply removing the the spaces   

# WE CAN SPECIFY THE NUMBER OF TIMES WE WANT TO IMPLEMENT THE SUBTITUTE FUNCTION ON OY STRING
print(' ')
x8 =re.sub("\s","2",intro,10)
print(x8)     #checking for that we can have 2 printed 10 times

# note that when it comes to searching elements from the string we have these three keywords in order to make them helpful with some stuff
# .span()
# .string()
# .group()

x10 =re.search(r"\bS\w+",intro)   #  raw string   #\b means beginning & S IS THE LAPHABET WE ARE LOOKING FOR w+ means words
print('\n',x10)     

x11 =re.search('\w',intro)      # simple 
print(x11)
print(x11.span())    #span from 0 to 1
print(x11.string)     # simply prints the string
print(x11.group())      # the true or false 

# using the character limit can also help to print the values from a limitede domain



# [A-Z] / The alphabets are printed if present in the string within the limited domain
print(" ")
x12 =re.findall("[A-D]",intro)
print(x12)   #  nothing gets printed 
print("     ")

# /d -> prints the numbers
x13 = re.findall("\d",x)
print(x13)      # simply sdisplaying the numberics present in the string understudy

# using the two dots would print the value understudy from the string
print(" ")
x14 =re.findall("MUHA..AD",intro)
print(x14)      # prints the full form and the ** values should  be the same alphabets

# ^ starting the elements
x15 = re.findall("^My",x)
#print(x15)     # simply presents that if the element start in the string or not 
if x15:
    print(True)
else:
    print(False)

print(" ")
x16 =re.findall("year$",x)
if x16:
    print(True)
else:
    print(False) 
print(' ')
x17 =re.findall('MUHA.*AD',intro)      # true
print(x17)

x18 =re.findall("MUHA.+AD",intro)     # DONE
print(x18) 
x19 =re.findall('MUHA.?AD',intro)    # none printed cuz there are two consecutive m's
print(x19)

# now searching for a word tha starts with scienc and ends with es lets see what it does
x20 =re.findall("MUHA.{2}AD",intro)
print(x20)

print('  ')
x21 =re.findall("NATURAL|SYNTHATIC",intro)
print(x21)
if x21:      # simply checks for the availablity of the element in the respective string under study
    print(True)
else:
    print(False)


# CHECKING FOR THE OTHER AVAILABLE BRACKETSS
x22 =re.findall("[ARN]",intro)
print('\n',x22)       # printing the values

x23 =re.findall("[A-G]",intro)
print('\n',x23)    #printing the alphabets in the string availablity

# PRINTING THE VALUES OR ALPHABETS THAT ARE NOT PRESENT IN THE [BRCKETS]
x24=re.findall("[^A-C]",intro)
print('\n',x24)    

x25 =re.findall("[29]",x)
print('\n',x25)   #simply checking for the presence of the 9 digit

x26 =re.findall("[0-9]",x)       #simple presence of the numbers in th strings understudy
print('')
print(x26)
if x26:
    print(True)
else:
    print(False)

x27 =re.findall("[0-5][0-9]",x)    #  the sting [2-5] the first element should be from 1 to 5
print(x27)

# checking for the upper as well as lower case study of the alphabets in the string

x28 =re.findall("[a-zA-Z]",intro)
print(x28)     #prints the all alphabets are present in the string

#   checking for the arithematic and logical expressions in the string
x29 =re.findall("[+]",in1)
print(' ')
print(x29)    # simple additional arithematic operator is present 