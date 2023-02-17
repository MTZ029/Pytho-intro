print('Talha')

#       unordered, unindexed , immutable
#       no repition allowed 

dost={"Talha","hassan","Kashif","Husnain","Sohaib","Hamzee","Ahmed","Daniyal","Rizvi'boy"}

nums= {12,22,22,41,90,87,67,54,40,'Husnain'}

dost.symmetric_difference_update(nums)
print('\n',dost,'\n')

B= {True ,True , True, False, False,False,False,True,True}

cars={'hyundai','BMW','Mercedes','Toyota','Subaru','Benz','Honda','hassan','Suzuki','IMPALA','FORD','Pontiac'}
print(dost,'\n',nums,'\n',B) # can't be refered to by indexing
# can be written by the set constructor set()

y=set(('BMX','PHOENIX','Champion'))
print(type(y))

for x in dost:
    print(x)   # simple printing 

# checking if and element is present in the set
 
print(22 in nums)      # true if 22 is present in the list named nums
# one set is created you can't add any new element in it

#   adding items in the list   -> simple add method
dost.add("maeeda")
print(dost)

# adding to set is note simple as using  +
dost.update(nums)
print(dost)   # simple yet unordered

#              important thing to remember is that the updating part is note necasarily a list as shown below:
y1="talha","carlover","Pakistani","Averagestudent",3.5,True         #tuple
nums.update(y1)
print('\n',len(nums))
print("Talha" in dost)

#   reemove item from the set or set empty as shown below :
nums.remove(40)         # simple removing the item from the set 
print(len(nums))

#   can also use discard method

B.discard(False)        # same as remove
print(B)

y.pop()
print(y)   # it removes oine elemnt from the set! but as the set is unordered, we don't know what we are removing
dost.pop()
print(dost)

#   clear method to clear all the elemnts of the set 
y.clear() 
print(y)        # phy set

#   difference between the set and del is that del eradicates set entirely, the set on the other hand resets all the elements of the set understudy
"""del y 
print(y)        #error """

# loops :

"""i=0
while i in dost:    # while loop doesn't work because unindexed
    print(i)
    i=i+1           """

for x in B:
    print(x)  # done simply

#        joining two or more sets together when we want to know the difference 
#                   -> union
un=dost.union(B)
print(un)
cars.update(dost)      # note that we can't equate it to any other set -> set3=caas.update(dost) not possible
print('\n',cars)

#           only similar elements present print         intersection_update() & intersection()
q1=set(("Apple","microsoft","thinkpad"))
q2=set(("microsoft","nokia","hp"))
cars.intersection_update(dost)
print('\n',cars)


q1.intersection_update(q2)
print(q1)         #done ->BEst no need for additional set to be included

#       if we want to print a new set, we use the intersection()    simply
q3 =q1.intersection(q2)
print(q3)

#           elements are not present in both the given sets, we use symmetri_difference_update()
q4=set((24,True,'hyundai'))
q5= set((24.0,False,'honda'))

q4.symmetric_difference_update(q5)
print('\n',q4)   # got it 

#           similarly if we want to print tall the elemnts except those are common, we print can introduce another set 
q6 =q5.symmetric_difference(q4)
print('\n',q6,'\n')

fruits={"apple","mango","lemon","tomato","peach"}
breakfast={"bread","eggs","chicken","paratha/tortilla","tea"}
nums2={12,22,34,54}
nums3={21,12,34,55}
num6={"t","e"}
num8={"r","f"}
#                           -> Methods:
#                              *->add()
#                              *->clear()
#                              *->copy()
#                              *->difference() =>not in y
#                              *->discard()
#                              *->isdisjoint   -> nothing in common
#                              *->issubset()-> true/false weather the concerned set is subset of other
#                              *->issuperset()  -> lower set is smaller than the upper set 
#                              *->symmetric_differnce()  remove the common elements
breakfast.add("pancakes")
print('\n',breakfast,'\n')   #done

breakfast.clear()
print(breakfast)

y2 =fruits.copy()
print(y2)

nums4=nums2.difference(nums3)     # their is not in update
print(nums4) 
#   can be done by difference_update()
nums3.difference_update(nums2)
print(nums3)
nums4.discard(54)       #atleast one input argument
print(nums4)

nums5 =nums3.intersection(num6)
print(nums5) 
nums7 =nums2.intersection( nums3, num6)
print('\n',nums7,'\n')

nums2.intersection_update( nums3,num6)
print(nums2)            #simple !   update    

x = num6.isdisjoint(num8)
print(" THIS IS X=>", x)      #independent or uncommon values in both the sets

aa={"a","b","c"}
aa1={"d","e","f","a","b","c"}
aa2={"s","e"}
o =aa.issubset(aa1)
print(o)            #->got it

o1=aa.issuperset(aa1)
o2=aa1.issuperset(aa2)
print(o1,o2)

xx =aa.symmetric_difference(aa1)
print(xx)      #SIMPLE

z=aa.union(aa2)
print(z)