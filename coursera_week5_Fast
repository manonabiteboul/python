import sys
import urllib.request
import os
import math
import binascii
import struct
import string
import array
import struct
import sys
import gmpy2
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes


#Constants

p=13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171

g=11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568

h=3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

B=pow(2,20)
print(B)

#Some functions:

#powmod(b,e,n) - Compute b^e mod n efficiently.
def powmod(b,e,n):
	"""powmod(b,e,n) computes the eth power of b mod n.  
	(Actually, this is not needed, as pow(b,e,n) does the same thing for positive integers.
	This will be useful in future for non-integers or inverses."""
	accum = 1; i = 0; bpow2 = b
	while ((e>>i)>0):
		if((e>>i) & 1):
			accum = (accum*bpow2) % n
		bpow2 = (bpow2*bpow2) % n
		i+=1
	return accum




#Testing the functions
print(powmod(3,2,6))
#mod 5:
print(27%5)

#Testing Hash functions
mon_dictionnaire = dict()
mon_dictionnaire["pseudo"] = "Manon"
mon_dictionnaire["mot de passe"] = "*"
print(mon_dictionnaire)

if "*" in mon_dictionnaire.values():
    print("* is a value")

if "pseudo" in mon_dictionnaire.keys():
    print("pseudo is a key, it is the key for " , mon_dictionnaire["pseudo"])



#Creating the Hash Table

hashT = dict()
for x1 in range(0,B):
    if x1%1000 == 0:
        print("x1 = ", x1)
    temp1 = powmod(g,x1,p)
    temp2 = powmod(temp1,p-2,p)
    temp3 = (temp2*h) % p
    hashT[x1] = temp3

print(x1)


#Step 2
for x0 in range(0,B):
    if x0%1000 == 0:
        print("x0 = ", x0)
    temp1 = powmod(g,B*x0,p)
    if temp1 in hashT.values():
        print("We have found the right x0: ", x0)
        x0final = x0
        break

print("This is x0final: ",x0final)
x=x0final * B +x1
xfinal = x % p
print("This is the solution: ", xfinal)

