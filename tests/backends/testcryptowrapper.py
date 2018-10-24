
from nacl_encrypted_fields.backends.cryptowrapper import CryptoWrapper

import base64


# Test class that uses XOR to encrypt. Requirements are to implement encrypt()
# and decrypt(). NOTE: do not use this in production.
class TestCryptoWrapper(CryptoWrapper):
    def __init__(self, keydata, *args, **kwargs):
        self.key = base64.b85decode(keydata)

    def encrypt(self, plaintext):
        return bytes([itr ^ self.key[idx % len(self.key)] for idx, itr in enumerate(plaintext)])

    def decrypt(self, ciphertext):
        return ''.join(chr(itr ^ self.key[idx % len(self.key)]) for idx, itr in enumerate(ciphertext))
