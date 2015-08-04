import os
import math
import binascii
import struct
import string
import array
import struct
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes

def xor(a,b):
    counter = 0
    result = ''

    if len(a) > len(b):
        a = a[:len(b)]
    else:
        b = b[:len(a)]

    for i in a:
        if i == '0':
            if b[counter] == '1':
                result = result + '1'
            else:
                result = result + '0'
        else:
            if b[counter] == '0':
                result = result + '1'
            else:
                result = result + '0'
        counter = counter + 1

    return result

def toBin(b):
    bi = bin(int.from_bytes(b, "big"))[2:]
    bi = '0' * (8 - (len(bi) % 8)) + bi

    return bi

def toText(bin): 
    i=0
    answer = '' 
    while i<len(bin):
        l = chr(int(bin[i:i+8],2))
        answer = answer+l
        i = i+8
    return answer

def toBytes(str1):
    i=0
    answer = b'' 
    while i<len(str1):
        strInt = int(str1[i:i+8],2)
        strB = struct.pack('>I', strInt)
        answer = answer+strB        
        i = i+8
    return answer

c='20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d '
cBytes = bytes.fromhex(c)
cBin = toBin(cBytes)
print(cBin)

h = 'Pay Bob 100$'
h100 = b'        100 '
h500 = b'        500 '

t100= binascii.hexlify(h100)
t500= binascii.hexlify(h500)
r100 = toBin(t100)
r500 = toBin(t500)
intermediate = xor(r100,r500)
resultBin = xor(intermediate, cBin)
print("result: ",resultBin)


myStr='10010101110010101'
x=int(myStr,2)
BITS_IN_BYTE = 8
b = bytearray(int(myStr[i:i+BITS_IN_BYTE], 2)
    for i in xrange(0, len(chars), BITS_IN_BYTE))

t=struct.pack('i',x)
print(t)
print(b)
