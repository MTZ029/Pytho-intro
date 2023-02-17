from asyncore import write


print(" TRY | EXCEPT    ")
#using ht etry funciton but would generate an error that x i not defined in the code

try:
    print(x)   # THE DEFINING ERROR OF PYTHON SIMPLY

except:
    print("  KNOCK KNOCK PHYSICS IS THE BEST    ")

try:
    print(x)
except NameError:
    print(" THE VALUE OF X IS NOT DEFINED   ")
except:
    print(" THIS IS TALHA   ")
# else use 

try:
    print(" ALOHA   ")
    #print(x)    gives the error
except:
    print("There is an error")   # simply works when there is no error simple
else:
    print("There is no error")

# the finally keyword working

print(' ')
try:
    print(x)
    print("Talha Zahid")

except:
    print('THERE IS AN ERROR    ')
finally:
    print("the finally keyword working")

print(" ")
try:
    f=open("Instruction.docs")
    try:
        write(" this is talha from python    ")
    except:
        print("something went wrong")
    finally:
        print(" envoking the finally blovck of the code  ")
except:
    print(" something else went wrong    ")

# note that the raise fiunction is used to raisean exception

x = -2
if x<0:
    raise Exception(" THE VALUE PRINTED WOULD BE ERROR ")      # this value is still printed 

a =input("  KINDLY ENTER THE VALUE YOU WANT TO CHECK WEATHER THE TYPE-ERROR EXISTS OR NOT   ")

if not type(a) in int:
    raise TypeError(" only integers allowed please ") #  REMOVE THE RUNNING ERROR TOMORROW ,
                                                      # NOte THAT WE NEED RUN THE LAST LOOP BEFORE GPOING TO THE NEW LOOP