
from nacl_encrypted_fields.backends.cryptowrapper import CryptoWrapper

from base64 import b85decode


# Test class that uses XOR to encrypt. Requirements are to implement encrypt()
# and decrypt(). NOTE: do not use this in production.
class TestCryptoWrapper(CryptoWrapper):
    def __init__(self, keydata, *args, **kwargs):
        self.key = bytearray(b85decode(keydata))

    def encrypt(self, plaintext):
        return bytes(bytearray([itr ^ self.key[idx % len(self.key)]
                     for idx, itr in enumerate(bytearray(plaintext))]))

    def decrypt(self, ciphertext):
        return bytes(bytearray([itr ^ self.key[idx % len(self.key)]
                     for idx, itr in enumerate(bytearray(ciphertext))]))
