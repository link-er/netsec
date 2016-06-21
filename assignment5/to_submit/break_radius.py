import hashlib

def xorWord(s0, s1):
  l = [ chr ( ord (a) ^ ord (b) ) for a,b in zip (s0, s1) ]
  return ''.join (l)

authent = '5631dc795c591b9fc78890c18ab74a29'
encr_pwd = '15efb479ae5bb57fdda1f2d011a51e18'

hashed = xorWord('0000000000000000', encr_pwd.decode('hex'))
with open('rfc7511.txt','r') as f:
  for line in f:
    for word in line.split():
      if hashlib.md5(word + authent.decode('hex')).digest() == hashed :
        print word
