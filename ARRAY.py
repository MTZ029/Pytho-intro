car= ['bmw','mercedes','audi','toyota','hyundai','honda','Subaru']
manufactrers =['america','japan','korea','china','India']
x =car[2]
three_d=[[[1,3],[2,3]],[['HONDA','Hyundai'],['TOYOTA','SUZUKI']],[[2.4,23.9],[3.099,44.2]]]
print(x)        #ARRAY

#   MODIFICATIONPF THE LIST
car[0]='PONtiAc'
print('\n',car)
print(len(car))   
#looping 
for x in car:
    print(x)
print(" ")
print(three_d)
for x in three_d:
    print(x)

for i in range(2):
    for k in range(2):
        for j in range(2):
                print(three_d[i][k][j])

print(" ")
car.append('impala')
print(car)

print(" ")
car.pop(3)
print(car)    

print(" ")
car.remove('PONtiAc')
print(car)      # the length decresases 

three_d.clear()
print(three_d)

z= car.copy()
print(z)

print(" ")
print(car.count('hyundai'))

print(" ")
car.extend(manufactrers)
print(car)

print(" ")
print(manufactrers.index('japan'))

print(" ")
car.insert(3,'kia')
print(car)

print(" ")
car.reverse()
print(car)            # simple reversal takes place 

print(" ")
car.sort()
print(car)         # sorting alpohabetically 