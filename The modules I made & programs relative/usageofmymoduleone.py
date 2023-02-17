import mymoduleone
import mymoduleone as mx
import platform

mymoduleone.bio(" Muhamad Talha Zahid   ")
print("module probelm solved for the use of a function")   # simply done 
 #note that the important point in this regard is that we need to have the both program s in the same doirectory as we creatre a new folder for this job

a =mymoduleone.myname
print(a)

print(' ')
b =mymoduleone.x      # simple lsit
print(b)

print(' ')
a1 =mx.y
print(a1)   # simply imported the alias

print(' ')
a2 =platform.system()
print(a2)      # letting us know the operating system being used by the device

print(' ')
a3 =dir(platform) 
print(a3)      #simple use of the dir 
# note that the dir function takes the input argument as platform


# NOte THAT WE CAN ALSO IMPORT ONLY ONE INPUT ACCORDING TO OUR NEEDS AS SHOW BELOW:

from mymoduleone import x
print(' ')
print(x)     # SIMPLY IMPORTED THE LIST WE WANT TO USE 