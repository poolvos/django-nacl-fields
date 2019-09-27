
import base64

# https://docs.python.org/3.5/library/base64.html#base64.b85encode
# https://github.com/git/git/blob/master/base85.c

CHARSET = bytearray(b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~')
DECDSET = [0] * 256


def _prep_decode_set():
    if DECDSET[ord('Z')]:
        return

    for idx, itr in enumerate(bytearray(CHARSET)):
        DECDSET[itr] = idx


def b85encode(plain):
    pad = 4 - (len(plain) % 4) if len(plain) % 4 else 0
    plain = bytearray(plain + pad * b'\x00')

    ret = b''
    for idx in range(0, len(plain), 4):
        num = int(base64.b16encode(plain[idx:idx + 4]), 16)
        arr = []
        while num:
            num, rem = divmod(num, 85)
            arr.append(CHARSET[rem])

        arr = bytearray(arr)
        ret += arr[::-1]

    return bytes(ret[:-pad]) if pad else bytes(ret)


def b85decode(encd):
    _prep_decode_set()

    pad = 5 - (len(encd) % 5) if len(encd) % 5 else 0
    encd = bytearray(encd + pad * b'~')

    ret = b''
    for idx in range(0, len(encd), 5):
        num = 0
        for jdx, itr in enumerate(encd[idx:idx + 5]):
            num += DECDSET[itr] * 85 ** (4 - jdx)

        ret += bytearray.fromhex(hex(num)[2:].zfill(8))

    return bytes(ret[:-pad]) if pad else bytes(ret)
