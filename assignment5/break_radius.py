import hashlib
import re

def xorWord(s0, s1):
  l = [ chr ( ord (a) ^ ord (b) ) for a,b in zip (s0, s1) ]
  return ''.join (l)

authent = '5631dc795c591b9fc78890c18ab74a29'
encr_pwd = '15efb479ae5bb57fdda1f2d011a51e18'

with open('rfc7511.txt','r') as f:
  for line in f:
    for word in line.split():
      clean_word = re.sub('[!@#$().,?\[\]]"\'', '', word)
      if xorWord('0000000000000000', hashlib.md5(clean_word + authent.decode('hex')).digest()) == encr_pwd.decode('hex') :
        print clean_word
      if xorWord('0000000000000000', hashlib.md5(word + authent.decode('hex')).digest()) == encr_pwd.decode('hex') :
        print word
      if xorWord('0000000000000000', hashlib.md5(clean_word + authent.decode('hex')).hexdigest()) == encr_pwd.decode('hex') :
        print clean_word
      if xorWord('0000000000000000', hashlib.md5(word + authent.decode('hex')).hexdigest()) == encr_pwd.decode('hex') :
        print word
