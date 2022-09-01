import hashlib
# Pamaos un valor str a binario y lo codificamos en MD5
def _hash(val):
    p_encode = val.encode()
    h = hashlib.new("md5", p_encode)
    password = (h.hexdigest())
    print (password)
    
_hash("!Contel#2018")