import os
import math
import binascii

def xor(a,b):
    counter =0
    for i in a:
        if counter==0:
            if i=='0':
                if b[0]=='0':
                    result='0'
                else:
                    result='1'
            else:
                if b[0]=='0':
                    result='1'
                else:
                    result='0'
            counter=1
        else:
            if i=='0':
                if b[counter]=='1':
                    result = result+'1'
                else:
                    result = result+'0'
            else:
                if b[counter]=='0':
                    result = result+'1'
                else:
                    result = result+'0'
            counter=counter+1             
    return result

def toText(bin):
    i=0
    answer = '' 
    while i<len(bin):
        l = chr(int(bin[i:i+8],2))
        answer = answer+l
        i = i+8
    return answer  


def result(b):
    r=''
    capitals = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    for i in b:
        if i in capitals:
            r=r+i
        else:
            r=r+'*'
    return r
       
    
	
m3=bytes.fromhex("32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb")
m1=bytes.fromhex("315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e")
m2=bytes.fromhex("234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f")
m4=bytes.fromhex("32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa")
m5=bytes.fromhex("3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070")
m6=bytes.fromhex("32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4")
m7=bytes.fromhex("32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce")
m8=bytes.fromhex("315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3")
m9=bytes.fromhex("271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027")
m10=bytes.fromhex("466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83")


tester1=bytes.fromhex("68656c6c6f20776f726c6421")
btester1 = bin(int.from_bytes(tester1, "big"))
print(btester1)
btester1=  btester1[0] + btester1[2:]
print(btester1)
t5 = toText(btester1)

print(t5)

#We go from hex to binary, and remove the second element which is a b for some reason(see above example for hello world)
b1=bin(int.from_bytes(m1, "big"))
b1 = b1[0]+b1[2:]
b2=bin(int.from_bytes(m2, "big"))
b2 = b2[0]+b2[2:]
b3=bin(int.from_bytes(m3, "big"))
b3 = b3[0]+b3[2:]
b4=bin(int.from_bytes(m4, "big"))
b4 = b4[0]+b4[2:]
b5=bin(int.from_bytes(m5, "big"))
b5 = b5[0]+b5[2:]
b6=bin(int.from_bytes(m6, "big"))
b6 = b6[0]+b6[2:]
b7=bin(int.from_bytes(m7, "big"))
b7 = b7[0]+b7[2:]
b8=bin(int.from_bytes(m8, "big"))
b8 = b8[0]+b8[2:]
b9=bin(int.from_bytes(m9, "big"))
b9 = b9[0]+b9[2:]
b10=bin(int.from_bytes(m10, "big"))
b10 = b10[0]+b10[2:]

#Truncate so everything has the same length as the shortest message m3
l = len(b3)
b1 = b1[:l]
b2 = b2[:l]
b4 = b4[:l]
b5 = b5[:l]
b6 = b6[:l]
b7 = b7[:l]
b8 = b8[:l]
b9 = b9[:l]
b10 = b10[:l]

#We are looking to decode the shortest msg m3, xor 
bb1=xor(b3, b1)
bb1 = toText(bb1)
print(bb1)

bb2=xor(b2, b1)
bb2 = toText(bb2)

bb4=xor(b3, b4)
bb4 = toText(bb4)

bb5=xor(b3, b5)
bb5 = toText(bb5)

bb6=xor(b3, b6)
bb6 = toText(bb6)

bb7=xor(b3, b7)
bb7 = toText(bb7)

bb8=xor(b3, b8)
bb8 = toText(bb8)

bb9=xor(b3, b9)
bb9 = toText(bb9)

bb10=xor(b3, b10)
bb10 = toText(bb10)






res1 = result(bb1)
print("b1 xor b3 : ",res1)
res2 = result(bb2)
print("b1 xor b4 : ",res2)
res4 = result(bb4)
print("b1 xor b5 : ",res4)
res5 = result(bb5)
print("b1 xor b6 : ",res5)
res6 = result(bb6)
print("b1 xor b7 : ",res6)
res7 = result(bb7)
print("b1 xor b8 : ",res7)
res8 = result(bb8)
print("b1 xor b9 : ",res8)
res9 = result(bb9)
print("b1 xor b10 : ",res9)
res10 = result(bb10)
print("b1 xor b3 : ",res10)

mylist = []
mylist.append(res1)
mylist.append(res2)
mylist.append(res4)
mylist.append(res5)
mylist.append(res6)
mylist.append(res7)
mylist.append(res8)
mylist.append(res9)
mylist.append(res10)

print(mylist[0][3])
capitals = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

sol = ''
for p in range(0,len(mylist[0])):
    count =0
    letter = ''
    for i in range(0,len(mylist)):
        #print(mylist[i][p])
        if mylist[i][p] in capitals:
            #print("this is a capital")
            if letter!=mylist[i][p]:
                count = count+1
                letter = mylist[i][p]
    if count==1:
        sol = sol+letter
    elif count ==0:
        sol = sol+'*'
    else:
        sol = sol+' '
    #print("sol:",sol)

print("this is sol: ", sol)



 #if i==len(mylist):
  #              print("but we are at the end so add letter and break")
   #             sol = sol + mylist[i][p]
    #            break
     #       else:
      #          print("not at end")
       #         for j in range(i+1,len(mylist)):
        #            print("so look at next")
         #           if mylist[j][p] in capitals:
          #              print("capital so break")
           #             sol = sol+' '
            #            break
#tester = input("type letter")
#if tester in capitals:
#    print("this is a capital")
#else:
#    print("nope")
#print(capitals)

#''.join(chr(int(bin_text[i:i+8], 2)) for i in xrange(0, len(bin_text), 8))

#binascii.a2b_uu(b)

#binascii.unhexlify('%x' % m1)



#os.system("pause")
