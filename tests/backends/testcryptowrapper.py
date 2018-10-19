
from fields.backends.cryptowrapper import CryptoWrapper

import base64


# Test class that uses XOR to encrypt. Requirements are to implement encrypt()
# and decrypt(). NOTE: do not use this in production.
class TestCryptoWrapper(CryptoWrapper):
	def __init__(self, keydata, *args, **kwargs):
		self.key = base64.b64decode(keydata)

	def encrypt(self, plaintext):
		enc = bytes([ord(itr) ^ self.key[idx % len(self.key)]
		             for idx, itr in enumerate(plaintext)])
		return base64.b64encode(enc).decode()

	def decrypt(self, ciphertext):
		enc = base64.b64decode(ciphertext.encode())
		return ''.join(chr(itr ^ self.key[idx % len(self.key)])
		               for idx, itr in enumerate(enc))
