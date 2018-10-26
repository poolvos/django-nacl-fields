
from nacl_encrypted_fields.backends.cryptowrapper import CryptoWrapper

import base64

import nacl.pwhash
import nacl.utils
import nacl.secret

from django.core.exceptions import ImproperlyConfigured


class NaClWrapperException(ImproperlyConfigured):
    pass


# Simple wrapper around PyNaCl to standardise the initialization of the box
# object and allow for others to extend as needed.
class NaClWrapper(CryptoWrapper):
    def __init__(self, keydata, apply_kdf=False, *args, **kwargs):
        key = base64.b85decode(keydata)
        if len(key) != nacl.secret.SecretBox.KEY_SIZE:
            raise NaClWrapperException('keysize must be equal to %d bytes', nacl.secret.SecretBox.KEY_SIZE)

        self.box = nacl.secret.SecretBox(key)

    def encrypt(self, plaintext):
        return self.box.encrypt(plaintext)

    def decrypt(self, ciphertext):
        return self.box.decrypt(ciphertext)

    @staticmethod
    def createKey():
        return base64.b85encode(nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE))
