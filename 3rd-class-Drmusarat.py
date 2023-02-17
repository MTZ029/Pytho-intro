
print("Assignment Dr.Musart")
str1="ISRO stand for “Indian Space Research Organization” (wkipedia n.d.). As the 20th century went half way through, the superpowers of the time started to play a part in the race of space and that was the time when the genesis of modern times organization ISRO took place inspired from the developed and well-equipped nations. The two Indian pioneer scientists “Homi Bhabha” (wkipedia n.d.) and “Vikram Sarabhai” (wkipedia n.d.) are considered as the father of ISRO as they took the initiative of making India part of the race that was integral for the future. In 1962 INCOSPAR {Indian National Committee For Space Research} was founded, which later became ISRO in 1969. ISRO in collaboration with other countries had already sent a lot of shuttles in the space and had a lot of experience in this regard. Some examples may include Aryabhata in 1975, Rohini in 1980, Chandaria-Chandaria-II and Mangalyaan. ISRO has total of three world records that have not been broken till date. First is the discovery of water on the moon. Second is the fact that India is the only nation in the whole wide world that reached mars without any sort of failures. Third record is the launch of a hundred and four satellites in one go! Mission Mangalyaan is the major setback that defines the company and help it to hold its firm grip over all other companies present related to field"
print(str1)


print("""PLease enter any one of the following:
    1-> find any alphabet
    2-> relpace 
    3-> append the given list
    4-> to split the given string
    """)

chice=int(input("enter the choice           "))

if chice==1:     #    == means equal
    print(" YOU CHOSE THE FIRST OPTION  ")
    print(str1.find('of'))
    # note that we can limit the finding are from the string by limiting it in some index as shown below
    print(str1.find('e',19,55))   #finding the alphabets in the limited place
    p1=str(input("\n please enter the alphabet to search \n"))
    print(str1.find(p1))
 
elif chice==2:
    print(" YOU COSE SECOND OPTION  ")
    print(str1.replace('of','OFF'))
    print(str1.replace('ISRO','SR'))
elif chice==3: 
    print(" YOU CHOSE THIRD OPTION  ")
    print("\n Please type the datat you want to append in the string given \n")
    s=str(input())
    print(str1.__add__(s))
   
elif chice==4:  
    print(" YOU CHOSE FOURTH OPTION")
    print(str1.rsplit(','))

else :
    print(" YOU CHOSE INVALID OPTION    ")
 
#note that the reason for using the elsif is that we dont want the last statement to be printed all the time 

#print(len(str1))

#function is an independent code 


b=65
print(ascii(str1))
for i in range(26):
    print(chr(b))
    b=b+1
   

talha="talha zahid"
print(talha.replace("a","c",2))

    #42 
t1="talha"
t=ord(t1[4])
t2=t-55
t3=chr(t2)
print(t1.replace(t1[4],t3))
print()

old_string = "aba"

string_list = list(old_string)   # convert to a list first 
string_list[2] = "c"
#Replace 3rd element

new_string = "".join(string_list)

print(new_string)



string13=[[[1,2],[4,7]],[[3,4],[9,6]]]
for i in range(2):
    for k in range(2):
        for j in range(2):
            string13[i][k][j]=str(input("integer aloowed only"))
           # print(string13[i][k][j])

print(string13)