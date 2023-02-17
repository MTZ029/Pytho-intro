import os
print('         file handlings      ')
print("  ")

"""
f =open("mode1.txt")  # specifyting the name of the function and letting the file to be opened and read and texted

# other sytax

f1 =open("mode1.txt","rt")
"""

fn =open("mode1.txt")
os.path.exists(fn)
print(fn.readlines())

