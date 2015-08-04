
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

#Bytes to Binary
def toBin(b):
    bi = bin(int.from_bytes(b, "big"))[2:]
    bi = '0' * (8 - (len(bi) % 8)) + bi

    return bi

#Binary to Text
def toText(bin): 
    i=0
    answer = '' 
    while i<len(bin):
        l = chr(int(bin[i:i+8],2))
        answer = answer+l
        i = i+8
    return answer

#Binary to Bytes
def toBytes(str1):
    i=0
    answer = b'' 
    while i<len(str1):
        strInt = int(str1[i:i+8],2)
        strB = struct.pack('>I', strInt)
        answer = answer+strB        
        i = i+8
    return answer

#Bytes to string of 1 and 0 to get 8 bits even if b is small (say 4)
def OneByteToBin(b):
    bi = bin(int.from_bytes(b, "big"))[2:]
    if len(bi)<8:
        bi = '0' * (8 - (len(bi) % 8)) + bi
    return bi


testerByte = '11100000'

print(toText(testerByte))


req = urllib.request.Request('http://crypto-class.appspot.com/po?er=f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb3')


cipherHex = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb3'

rest = 'http://crypto-class.appspot.com/po?er='


print("len of cipher Hex: ", len(cipherHex))
nbBytes = len(cipherHex)/2
print("This is the number of bytes:", nbBytes)

cipherBytes = bytes.fromhex(cipherHex)
print("len of cipher Bytes: ", len(cipherBytes))
cipherBin=toBin(cipherBytes)
print("len of cipher Binary: ", len(cipherBin))
print(cipherBin)

print("Testing  the first bite is good:")

g='01001101'
one = 1
oneB =  struct.pack('>I', one)
oneBin = OneByteToBin(oneB)
lastByte = cipherBin[512:]
a = xor(oneBin,lastByte)
b = xor(a, g)

test = toBytes(b)
test2 = ''.join(hex(b)[2:] for b in test)
print(test2)

req = urllib.request.Request('http://crypto-class.appspot.com/po?er=f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeff')
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    error = e.reason
    if error == 'Forbidden':
        print("This is the error: ",error)
    else:
        print("error: ", error)
        print("Found the good byte: ",test3,"g:",g, " as binary " , gBin)
        




one = 1
oneB =  struct.pack('>I', one)
oneBin = OneByteToBin(oneB)
print("this is 1: ", oneB, " in bin ",oneBin)
lastByte = cipherBin[512:]




t = 15
tB =  struct.pack('>I', t)
tBin = OneByteToBin(tB)
test = toBytes(tBin)
test2 = ''.join(hex(b)[2:] for b in test)
test3 = test2[3:]
if len(test3)<2:
    test3 = '0'+test3
print("This is a test for 15 ", test3)

#Finding the first byte
length = len(cipherHex)
g=76
lastByte = cipherBin[512:]
while g<256:
    gB =  struct.pack('>I', g)
    gBin = OneByteToBin(gB)
    print("g : ",g,"as bin : ", gBin)
    intermediate =xor(lastByte, gBin)
    xorLastByte = xor(intermediate,oneBin)
    g = g+1
    test = toBytes(xorLastByte)
    test2 = ''.join(hex(b)[2:] for b in test)
    test3 = test2[3:]
    if len(test3)<2:
        test3 = '0'+test3
    print("This is the new last bytes ", test3)
    newcipher = cipherHex[:length-2]+test3
    newWeb = rest+newcipher
    req = urllib.request.Request(newWeb)
    try: urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        error = e.reason
        if error == 'Forbidden':
            print("This is the error: ",error)
        else:
            print("error: ", error)
            print("Found the good byte: ",test3,"g:",g, " as binary " , gBin)
            break


#The good first byte is :01001101



step = 2
done = '01001101'
print("NEW STEP")

while step<3:
    print("step = ", step)
    stepB =  struct.pack('>I', step)
    stepBin = OneByteToBin(stepB)
    pad = ''
    for i in range(0,2):
        pad = pad+stepBin
        
        
    #print("StepBin: ", stepBin)
    print("and pad: ", pad)

    #reset to g=0
    g=150
    length = len(cipherHex)
    lengthBin = len(cipherBin)
    lastBytes = cipherBin[lengthBin-8*step:]
    print("This is cipherBin: ", cipherBin)
    print("These are the last Bytes: ", lastBytes)
    
    #print("this is length:", lengthBin, " and i used 512: and will now use: ", lengthBin-8*step)
    while g<256:
        if g%50==0:
            print("g= ", g)
        gB =  struct.pack('>I', g)
        gBin = OneByteToBin(gB)
        #print("and this is g in binary: ", gBin)
        #print("and this is g+done in binary: ", gBin+done)
        
        #print("g : ", gBin)
        
        intermediate =xor(lastBytes, gBin+done)
        xorLastBytes = xor(intermediate,pad)
        #print("pad      :", pad)
        #print("lastBytes:", lastBytes)
        #print("g+done   :", gBin+done)
        
        print("Which gives the following xorLastBytes", xorLastBytes)
        
        test = toBytes(xorLastBytes)
        test2 = ''.join(hex(b)[2:] for b in test)
        
        print("this is the before chosing letters : ",test2)
        if len(test2)%5 !=0:
            test2 = test2[0:5]+'0'+test2[5:]
            print("We have modified the letters to:", test2)
        
        
        increment = 3
        test4 =''

     
        while increment<len(test2):
            test4 = test4+ test2[increment:increment+2]
            increment = increment+5
       
        print("this is the new ciphertext letters : ",test4)  
        
        newcipher = cipherHex[:length-2*step]+test4
        newWeb = rest+newcipher
        req = urllib.request.Request(newWeb)
        try: urllib.request.urlopen(req)
        except urllib.error.URLError as e:
            error = e.reason
            if error == 'Forbidden':
                manon =0
                print("STEP 2 : This is the error: ",error)
            else:
                print("STEP 2 : Found the good byte: ",test4,"g:",g, " as binary " , gBin, "as text :", toText(gBin))
                break
        g= g+1
    done = gBin+done
    print("This is done: ", done)
    step = step+1

print("This is done:", done)
print("newWeb:", newWeb)

print("DONE!!!!")

#g=0
#lastByte = cipherBin[512:]
#while g<256:
#    gB =  struct.pack('>I', g)
#    gBin = OneByteToBin(gB)
#    print("g : ", gBin)
#    intermediate =xor(lastByte, gBin)
#    xorLastByte = xor(intermediate,oneBin)
#    g = g+1
#    t
#    test = toBytes(xorLastByte)
#    test2 = ''.join(hex(b)[2:] for b in test)
#    test3 = test2[3:]
#    if len(test3)<2:
#        test3 = '0'+test3
#    #print("This is the new last bytes ", test3)
#    newcipher = cipherHex[:length-2]+test3
#    newWeb = rest+newcipher
#    req = urllib.request.Request(newWeb)
#    try: urllib.request.urlopen(req)
#    except urllib.error.URLError as e:
#        error = e.reason
#        if error == 'Forbidden':
#            print("This is the error: ",error)
#        else:
#            print("Found the good byte: ",test3,"g:",g, " as binary " , gBin)
#            break


TesterDone = '1110000001001101'
print("This is the testerDone: ", TesterDone)
        


try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    error = e.reason
    if error == 'Forbidden':
        print("This is the error: ",error)
    else:
        print("Found the good byte")
        
