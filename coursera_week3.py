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



f = open("intro.mp4", "rb")
video=b''
i=0
dim =os.path.getsize("intro.mp4")
f=open("intro.mp4", "rb")
video = f.read(dim)
print("dim: ", dim)
dimVideo =len(video) 
print("dimVideo = " , dimVideo, "and type ", type(video))
blocksAprox = dimVideo/1024
blocks = 12202
print("This is the number of blocks: ", blocksAprox, "mod: ",dimVideo%1024 ,"so : ", blocks)


#the hash value is sometimes called the message digest

step = 1
b2 = video[(blocks-step)*1024:]

hash = SHA256.new()
hashed = hash.update(b2)
print("1: ",hash.digest())
hashed = hash.digest()
print("Test : ", binascii.hexlify(hashed))
step=2

while step<blocks+1:
    #print("step: ",step)
    b = video[(blocks-step)*1024:(blocks-(step-1))*1024]
    #print(len(b))
    b= b+hashed
    hash = SHA256.new()
    hash.update(b)
    
    #print("3: ",hash.digest())
    hashed = hash.digest()
    step = step+1

print(step)
print("sol: ",binascii.hexlify(hashed))
