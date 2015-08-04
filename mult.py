import os
import math

def table(nb, min=1, max=10):
	i=min
	while i<max+1:
		print(i, " * ", nb , " = ", i*nb)
		i+=1

def carre(n):
	return n*n

def pr(n):
	print("On est ds mult et n =",n)
	
if __name__=="__main__"	:
	table(8)
	os.system("pause")