print("If else statement")
# rules for if else statement
#                       ->a=b   equal
#                       ->a!=b not equal 
#                       ->a>b a greater 
#                       ->a=>b a greater equalt to 
#                       ->a<b b greater
#                       ->a<=b b greater equal to     

a=int(input("enter the value of a           "))
b=int(input("Enter the vaue of b            "))
c=int(input("enter the value of for later   "))

#       IF WE COMPARE 3 ELEMENTS

if a>b and c>a:
    print('\n',"    both conditions are true   ",'\n')
else:
    print(" B0TH CONDITONS ARE NOT TRUE ")

if a > b :
    print("a is grether than b")
elif a ==b:
    print(" a and b are equal ") 
else:
    print(" b is greater    ")
#      take care of the intendation if the intendation goes wrong there would be ajn error

#       shorthand for the if/else statement can be :
print(" ")

x = input("enter the value of x ")
y = input("enter the value of y ")
if x > y:print(" x i greater")
elif x < y:print(" y i greater")
else :print(" both are equal  ")

#   shorthand for the 3 different elements as shown above:

# lets make a software that compares the lenght of two strings 

a1 =str(input("  kindly enter the 1st paragarph     "))
a2 =str(input("  kindly enter the 2nd pararaph to compare with  "))
a3 =len(a1)
a4=len(a2)
# CHECKING FOR THE TWO INPUTS WITH ONE OF THE CONDITION IS TRUE
if a3>a4 or a4>a3:
    print("\n","    ONE OF THE CONDITON IS TRUE     ",'\n')

#   short hand
print(" Equal ") if a3==a4 else print(" 1st para is greater ") if a3>a4 else print(" 2nd paragraph is greater   ")

a5 =24.5
a6 =24
print("  BOTH ARE QUAL  ") if a5==a6 else print(a5," is greater") if a5>a6 else print(a6,'  is greater ')

#   NESTED IF/ESLE FUNCTIONS
x2 =int(input("enter the value below 10"))
if x2<10:
    print(x2,"  IS SMALLER THAN 10  ")
    if x2<20:
        print(x2,"  IS SMALLER THAN 20 TOO  ")
        if x2<30:
            print(x2,"  IS SMALLER THAN 30 TOO  ")
        else:
            ("  SMALLER ")

#           NOT THAT pass is used to pass the if statement empty, it removes the error
x4 =10
if x4>10:
    pass      # just to remove the error