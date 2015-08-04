import os
import math
import mult


a="1A2B3C"
n=0
counter = len(a)-1
result = 0
for i in a :
	print(i)
	if i=="A":
		n=10
	elif i=="B":
		n=11
	elif i=="C":
		n=12
	elif i=="D":
		n=13
	elif i=="E":
		n=14
	elif i=="F":
		n=15
	else:
		i=int(i)
		n=i
	print("counter = ", counter, ": The result is ", result, "and i is ", i , " and n is ", n , "so we increment by ",n* pow(16,counter))
	result=result+n* pow(16,counter)
	counter=counter-1
	
print(result)





n=input("Donne un chiffre")
n=int(n)
mult.pr(n)





a=mult.carre(3)
b=math.sqrt(a)
print(a)
print(b)	
		
mult.table(2)
mult.table(5, 2 , 4)


f=lambda a,b,c: a+b+c
a=f(1,2,3)
print("En utilisant lambda: ", a)

i=input("Enter a number")
i=int(i)
while i<10:
	i+=1
	
print("Now i is bigger then 10: ",i)

seq = "Salut"


	
for l in seq:
	print(l)
	
os.system("pause")