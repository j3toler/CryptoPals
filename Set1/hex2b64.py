from binascii import *

def hex2base64(string):
    """
       MISSING DESCRIPTION
    """
    answer = b2a_base64(unhexlify(string))
    return answer
