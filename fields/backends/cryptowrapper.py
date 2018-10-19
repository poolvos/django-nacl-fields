
class CryptoWrapper(object):
	def encrypt(self, plaintext):
		raise NotImplementedError

	def decrypt(self, ciphertext):
		raise NotImplementedError
