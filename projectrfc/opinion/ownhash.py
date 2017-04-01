from hashlib import sha224
import datetime

def sha(s):
    return sha224(s.encode("utf-8")).hexdigest()

def sha_t(s):
    return sha(s + str(datetime.datetime.now().timestamp()))
