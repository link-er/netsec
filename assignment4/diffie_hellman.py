import socket
import base64
import hashlib

TCP_IP = 'blue'
TCP_PORT1 = 3333
TCP_PORT0 = 4444
BUFFER_SIZE = 1024

def xorWord(s0, s1):
  l = [ chr ( ord (a) ^ ord (b) ) for a,b in zip (s0, s1) ]
  return ''.join (l)

s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s0.connect((TCP_IP, TCP_PORT0))
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((TCP_IP, TCP_PORT1))

msg = s0.recv(BUFFER_SIZE)
print str(TCP_PORT0) + ' : ' + msg
s1.send(msg)
msg = s1.recv(BUFFER_SIZE)
print str(TCP_PORT1) + ' : ' + msg

s0.send(msg)
msg = s0.recv(BUFFER_SIZE)
print str(TCP_PORT0) + ' : ' + msg
p = msg.split(' ')[4]
g = msg.split(' ')[8]
print '====================Got prime ' + str(p) + ' and generator ' + str(g)
my_prime = 3
s1.send(msg)

msg = s1.recv(BUFFER_SIZE)
print str(TCP_PORT1) + ' : ' + msg
k1 = msg.split(' ')[-2]
print '====================Got ' + str(TCP_PORT1) + ' key ' + k1
my_G = (int(g) ** my_prime) % long(p)
ar = msg.split(' ')
ar[-2] = str(my_G)
my_msg = ' '.join(ar)
print '====================' + my_msg

s0.send(my_msg)
msg = s0.recv(BUFFER_SIZE)
print str(TCP_PORT0) + ' : ' + msg
k0 = msg.split(' ')[-1][0:-2]
print '====================Got ' + str(TCP_PORT0) + ' key ' + k0
ar = msg.split(' ')
ar[-1] = str(my_G) + '!'
my_msg = ' '.join(ar)
print '====================' + my_msg

s1.send(my_msg)
msg = s1.recv(BUFFER_SIZE)
print str(TCP_PORT1) + ' : ' + msg
s0.send(msg)

my_k1 = (long(k1) ** my_prime) % long(p)
hash_my_k1 = hashlib.sha512(str(my_k1)).digest()
my_k0 = (long(k0) ** my_prime) % long(p)
hash_my_k0 = hashlib.sha512(str(my_k0)).digest()

msg = s0.recv(BUFFER_SIZE)
print str(TCP_PORT0) + ' : ' + msg
decrypted = xorWord(base64.b64encode(msg), hash_my_k0)
print 'Decrypted: ' + decrypted
my_msg = base64.b64encode(xorWord(decrypted, hash_my_k1))

s1.send(my_msg)
msg = s1.recv(BUFFER_SIZE)
print str(TCP_PORT1) + ' : ' + msg


s0.send(msg)
msg = s0.recv(BUFFER_SIZE)
print str(TCP_PORT0) + ' : ' + msg
s1.send(msg)
msg = s1.recv(BUFFER_SIZE)
print str(TCP_PORT1) + ' : ' + msg
s0.send(msg)
msg = s0.recv(BUFFER_SIZE)
print str(TCP_PORT0) + ' : ' + msg
s1.send(msg)
msg = s1.recv(BUFFER_SIZE)
print str(TCP_PORT1) + ' : ' + msg

s0.close()
s1.close()
