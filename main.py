def strtohex(a):
  return int(a, base=16)
  
def xor (a,b) :
  return hex(a ^ b)

def hextoascii(a):
  print(a)
  return bytearray.fromhex(a[2:]).decode()
  

#xor the key with message
listofmessage =[0x000d16251c07044b36171c0307280858291403500a2003450029001e5930070e52,
0x0d0d15713c49000a2c521d120f224f0125004d00163d100011380d0359330a0b4d,
0x151f00221a04064b2d1c0a571a2f021d6a050c145326054505231311102a084701,
0x0d091c71020c4308231c4f1a0f2d0a582c0003501c295624103e0008592a001001,
0x1d480d3e050c43052d521c031b220a163e550e111d6f04001328410e112d1c4701,
0x00000425551e0c1e2e164f150b661e0d2301085016221404003e00090a2d010001,
0x181d063a1c051a4b0d263f5707354f082f070b15103b1a1c523f04190b211b4701,
0x1001013f0149220930131d571d2716583e1d0802166f0104016c005a1a251b0449,
0x19091c3310491a0e365226570a2f0b163e551d110a6f171106290f0e102b014701,
0x030d45221d06160726521d120f2a03016a190403072a18450623413b1b360e1501,
0x1a090d71020c430a30174f13012f011f6a02081c1f6f010c06240e0f0d64070253]

message = '4E696B6F734E696B6F734E696B6F734E696B6F734E696B6F734E696B6F734E69'

#xor hexidecimal 

#message = Nikos = 4E696B6F73

#xor the key and the message
#use a for loop to go through the messages increment of 2

for x in range(10):
  for i,y in enumerate(listofmessage):
    temp = xor(strtohex(message),y)
    hextoascii(temp)
    message = '0' + message[:-1]