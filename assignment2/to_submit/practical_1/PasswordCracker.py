import passlib.hash
salt = "/pE9u4cQ" #salt is the value between 2nd and 3rd "$" of hashed password
key = "$apr1$/pE9u4cQ$ZfQfXfZ8NWh2gfFpIx22T0"
with open('data','r') as f:
    for line in f:
        for word in line.split():
            crypted = passlib.hash.apr_md5_crypt.encrypt(word, salt=salt)
            if(crypted==key):
                print "passwd found"
                print word






