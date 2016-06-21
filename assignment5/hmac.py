import hashlib


name2key = "90bed83e6b"
# as i am not sure, whether we should convert to ASCII before passing key to hmac, or inside of it
# i still leave this commented string below
#key = ''.join(str(ord(c)) for c in name2key)

# i have pdf file inn the same repository with this python file
in_file = open("netsec2016_exercise_sheet_05.pdf", "rb") # opening for [r]eading as [b]inary
data = in_file.read() # message - bytes string of pdf file
in_file.close()



def hmac(key, message):
    m = hashlib.sha1()
    block_size = m.block_size
    key = ''.join(str(ord(c)) for c in key) #ASCII representation of a string
    if len(key) > block_size: # if key is to large, make it block_size by hashing
        key = hashlib.sha1(key).digest()
    elif len(key) < block_size: # if key is too small, pas with leading zeros
        key = bytes(0x00) * (block_size - len(key)) + bytes(key)

    o_pad_value = 0x93
    i_pad_value = 0xA5

    key_bytes = bytearray(key)
    o_key_pad = bytearray(len(key_bytes))
    i_key_pad = bytearray(len(key_bytes))
    for i in range(len(key_bytes)):
        o_key_pad[i] = o_pad_value ^ key_bytes[i] # xor with opad
        i_key_pad[i] = i_pad_value ^ key_bytes[i] # xor with ipad

    return hashlib.sha1(str(o_key_pad) + hashlib.sha1(str(i_key_pad) + message).digest()).hexdigest() # hash(opad xor key concat hash(ipad xor key concat message)

print hmac(name2key, data)
