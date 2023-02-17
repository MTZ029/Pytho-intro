print(" WHILE LOOP")
#            Print elements from 0 to 6 
i=0
while i<7:
    print(i) 
    i += 1          # simply i=i+1
print(" ")
j =1
while j<10:
    print(j)
    if j==7:
         break   # out of the loop 
    j+=1                    # simply checking for the elements that are saller than 7
print(" ")

#       if we want to continue the printing precess except one , we use cotinue

k=0
while k<50:
    k +=1
    if k==30:
        continue
    print(k)

#           using the else statement 
print(" ")
l=0
while l<13:
    print(l)
    l+=1
else:
    print("L IS NO LONGER SMALLER THAN 13      ")
