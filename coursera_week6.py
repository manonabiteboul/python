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
from decimal import Decimal


#Inverse
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def multiplicativeInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
#Constants

N1 = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581

#Tests
print("test")
print(169.0%1)
print(38.509658609%1)

#Challenge 1

gmpy2.get_context().precision=1030

temp = gmpy2.sqrt(N1)

#print("t = ", temp)

A=   gmpy2.ceil(temp)

print("A = ", A)

temp2 = A*A

temp3 = temp2-N1

x = gmpy2.sqrt(temp3)

p=A-x
p4 = p
print("p= ",p)
q=A+x
q4 = q
print("q= ",q)
print("N1  = ",N1)
print("p*q = ", p*q)


if N1==p*q:
    print("True")


#Challenge 2


print("")
print("Challenge number 2")
N2 = 648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877

gmpy2.get_context().precision=1030

temp = gmpy2.sqrt(N2)

ALower=   gmpy2.ceil(temp)
up = pow(2,20)
A=ALower
while A<ALower+up:
   # print("A =", A)
    temp2 = A*A
    temp3 = temp2-N2
    x = gmpy2.sqrt(temp3)
    if x%1==0:
        p=A-x
        q=A+x
        if N2==p*q:
            print("We have factored N2: ")
            print("p = ", p)
            print("q = ", q)
            print("p*q = ", p*q)
            print("N2  = ", N2)
            break;
    A = A+1



    
#Challenge 3
print("")
print("This is challenge 3 :")

N3 = 720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929

gmpy2.get_context().precision=1030

temp = gmpy2.sqrt(N3)

print("N3 = ",N3)
print("t  = ", temp*temp)

A=   gmpy2.ceil(temp)

print("A = ", A)

temp2 = A*A

temp3 = temp2-6*N3

x = gmpy2.sqrt(temp3)
print(x)

ptest=A-x
print("p= ",ptest)
qtest=A+x
print("q= ",qtest)
print("N1  = ",6*N1)
print("p*q = ", ptest*qtest)


if N1==p*q:
    print("True")


#Challenge 4

print("This is challenge 4")
c = 22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540
N= 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581
p= 13407807929942597099574024998205846127479365820592393377723561443721764030073662768891111614362326998675040546094339320838419523375986027530441562135724301
q= 13407807929942597099574024998205846127479365820592393377723561443721764030073778560980348930557750569660049234002192590823085163940025485114449475265364281
if N==p*q:
    print("True")
e=65537
phiN = (p-1)*(q-1)
print("phiN: ", phiN)
d = multiplicativeInverse(e, phiN)
a = (e*d )%phiN
print("This i a : ", a)
if (e*d )%phiN==1:
    print("True2")
print("d = ",d)
m = pow(c,d,N)
print("m= ",m)
messageHex = hex(m)
print("message = ", messageHex)
mB = bytes.fromhex("0"+messageHex[2:])
print(mB)
