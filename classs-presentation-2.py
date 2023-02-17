#from traceback import print_tb
fruits = [4, 55, 64, 32, 16, 32]

#x = fruits.index(32, 2 , 4)
#0,1,2
#Checking for the index
#print(x)
#z=fruits.append(2, 'mango')
#print(z)


str="Name is Khan and I am not a {cast} and I have {money:.5f}".format(cast="terorist", money=200000)# f IS only envoked for integer
print(str)

print("\n")
stri="i have {:,}".format(2000000)
print(stri)

st="our earning varies from {:+} to {:+}".format(20 , 40)
print(st)

sss="The vehicle is {car} , brand is from {brand} and the cost is {cost}"
dictionar={'car':'toyota','brand':'honda','cost':'2000000'}
z=sss.format_map(dictionar)
print(z)

print('#'.join(str))
m=str.ljust(200)
print(m , 'medz')

pri="Talhaisthebest"
pri2="Is he though ?"
l=pri.ljust(80)
print(l,'Pakistan is the best')
print(pri.lower())

x="o".join(pri2)
print(x)

oo=pri.maketrans('a','P')
print(pri.translate(oo))

print('o'.join(pri))

rp2=pri.rjust(200,'i')
print(rp2)

print("\n")
za=pri.strip('talhbest')
print("Answer is",za,"BMW")

p=("bAHRIA","APS","Shaheen","USwa","Beacon")

(s1,s2,s3,s4,s5) = p
print('\n',s1,'\n')
p1=list(p)
p1[2]="Step"
p=tuple(p1)
print(p)
m=("QAU",)

p2=list(p)
p2.append('Head Start')
p=tuple(p2)
print(p)

p +=m
print(p)

for x in range(len(p)):
    print(p[x])
print(" ")
i=0
while i<len(p):
    print(p[i])
    i=i+1