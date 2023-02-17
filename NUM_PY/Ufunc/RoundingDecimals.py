print("Talha")
import numpy as np
# the decimal rounding off methods are solved by the following methods:
#    truncation   -> trunc()
#    fix()
#    rounding()
#    floor()
#    ceil()

# trunc()
arr =np.trunc([-3.1232, 3.14])
print("\n",arr)   # similar to floor function

# floor()

arr1 =np.floor([-3.123 , -81.123 ,  343])
print("\n",arr1)  # simply returns the floated amount

#rounding()

arr2 =np.around(3.1656666 , 2)  # it would only print the rounded off version of the value to 2nd decimal point 
print("\n",arr2)

# floor() -> function as studied in descreate mathematics

arr3 =np.floor([-3.05 , 2.4])   # floor function the lower value 
print("\n",arr3)

# ceil()  -> function same as descrete mathematics

arr4 =np.ceil([-3.12 , 4.13])  # greater value printeed 
print("\n",arr4)