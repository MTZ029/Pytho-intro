import datetime
print('     THE TIME AND DATE FUNCTIONS OF PYTHON   ')
y =datetime.datetime.now()
print('\n', y )       #it prints the current time and date of the same time the program runs

x=datetime.datetime.now()
print(x.year)
print(' ')
print(x.strftime('%A'))    # prints the complete name of the day of the week


# note that the object created has alot of different references as shown in the table w3school or you can also seee on the register

x1 =datetime.datetime(2022,8,10)       # no time printed in it the default of timezone is 0
print(' ')
print(x1)

x2 =datetime.datetime(2002 , 4 ,16)
print(' ')
print(x2.strftime('%B'))       # simple 


x4 =datetime.datetime(2002 ,4, 16)
print(' ')
print(x4.strftime('%Y'))    # simple