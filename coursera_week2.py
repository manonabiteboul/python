import os
import math
import binascii
import struct
import string
import array
import struct
import sys
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes
#import base16


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



str= '01234567890'
print(str[0:3])
print(str[3:7])
str2 = '11111111'
strInt = int(str2[0:8],2)
strB = struct.pack('i', strInt)
print ("This is new ", strB)
print("This is it's len ", len(strB)," and l2 : ")

print("NEW TEST")
hex_string = 'de ad be ef 00'
result = bytearray.fromhex("de ad be ef 00")
print("WTF ", result)

#result= array.array('B', hex_string.decode("hex"))
#print("ONE: ", result)
#result= bytearray(hex_string.decode("hex"))
#print("TWO: ", result)

SECRET_KEY = u'140b41b22a29beb4061bda66b6747e14'
length = len(SECRET_KEY)
print("LEN:",length)

key1Hex =bytes.fromhex('140b41b22a29beb4061bda66b6747e14')
key1Test =  bytes.fromhex('140b41b22a29beb4061bda66b6747e14')
print("key1Test!!: ", key1Test)

key1Str = toBin(key1Hex)
print("key1Str:", key1Str)
#key1 =toBytes(key1Str)
#print("size : ", sys.getsizeof(key1) ," and KEy1 : ",key1)

#l=len(key1)
#typ=type(key1)
#print("TYPE: ",typ)

cipher = AES.new(key1Test)

c1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'

print("Length of cipher1 ", len(c1))
block=32
length = len(c1)
print("The cipher has length ", length)
b=length / 16
print("There are ", b, " blocks")
IV = c1[0:16]
print("IV: ", IV, " and it's length: ", len(IV))
prev = IV
result = ''
step = 1

while step<b:
    block1 = c1[step*16:step*16+16]
    dec = cipher.decrypt(block1)
    dec = toBin(dec)
    x = xor(prev, dec)
    result = result+x
    step = step+1

print(result)
text = toText(result)
print(text)




#CBC mode
print("CBC mode ")
keyHex = '140b41b22a29beb4061bda66b6747e14'
keyBytes=bytes.fromhex(keyHex)
cHex = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
cBytes = bytes.fromhex(cHex)
cipher = AES.new(keyBytes)
L=len(cBytes)
print("This is Length: ",L)
b= 4
IV = cBytes[0:16]
IVBin = toBin(IV)
c0 =cBytes[16:32]
c1 =cBytes[32:48]
c2 = cBytes[48:64]
Dc0 = cipher.decrypt(c0)
Dc1 = cipher.decrypt(c1)
Dc2 = cipher.decrypt(c2)
c0Bin = toBin(c0)
c1Bin = toBin(c1)
c2Bin = toBin(c2)
Dc0Bin = toBin(Dc0)
Dc1Bin = toBin(Dc1)
Dc2Bin = toBin(Dc2)
m=''
m0 = xor(IVBin,Dc0Bin)
m = m+toText(m0)
m1 = xor(c0Bin,Dc1Bin)
m = m+toText(m1)
m2 = xor(c1Bin, Dc2Bin)
m = m+toText(m2)
print("This is the message: ", m)


cHex2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
cBytes = bytes.fromhex(cHex2)
cipher = AES.new(keyBytes)
L=len(cBytes)
print("This is Length: ",L)
b= 4
IV = cBytes[0:16]
IVBin = toBin(IV)
c0 =cBytes[16:32]
c1 =cBytes[32:48]
c2 = cBytes[48:64]
Dc0 = cipher.decrypt(c0)
Dc1 = cipher.decrypt(c1)
Dc2 = cipher.decrypt(c2)
c0Bin = toBin(c0)
c1Bin = toBin(c1)
c2Bin = toBin(c2)
Dc0Bin = toBin(Dc0)
Dc1Bin = toBin(Dc1)
Dc2Bin = toBin(Dc2)
m=''
m0 = xor(IVBin,Dc0Bin)
m = m+toText(m0)
m1 = xor(c0Bin,Dc1Bin)
m = m+toText(m1)
m2 = xor(c1Bin, Dc2Bin)
m = m+toText(m2)
print("This is the message: ", m)


#CTR mode
print("CTR MODE")


CTRkeyHex = '36f18357be4dbd77f050515c73fcf9f2'
CTRkey =  bytes.fromhex(CTRkeyHex)
CTRcHex = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
CTRcBYTES = bytes.fromhex(CTRcHex)
print("This is the length of the cipher: ", len(CTRcBYTES))
CTRcipher = AES.new(CTRkey)
#CTRcBIN = toBin(CTRcHex)
L = len(CTRcHex)
print("This is the length:", L)
print(CTRcBYTES[15])
IVBYTES = CTRcBYTES[0:16]
step = 0
m = ''
ct = CTRcBYTES[16:32]
print("KEY: ", len(CTRkey))
print("ct : ", len(ct))
decIV = CTRcipher.encrypt(IVBYTES)
decIVbin = toBin(decIV)
c0toBin = toBin(ct)
res = xor(decIVbin,c0toBin )
result = toText(res)
print("This is the result: ", result)


L=12
step = 2

while step<L:
    IV1 = bytes_to_long(IVBYTES)
    IV1 += step-1
    IV1 = long_to_bytes(IV1)
    ct = CTRcBYTES[step*16:step*16+16]
    decIV = CTRcipher.encrypt(IV1)
    decIVbin = toBin(decIV)
    c0toBin = toBin(ct)
    res = xor(decIVbin,c0toBin )
    res = toText(res)
    print("This is the result: ", res)
    result = result+res
    step=step+1
    
