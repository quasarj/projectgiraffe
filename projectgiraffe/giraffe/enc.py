# encrytpion fuctions, becuase apparently we are living in the dark ages

from Crypto.Cipher import AES
import binascii

def encrypt(key, plaintext):
     
    encobj = AES.new(fix_key(key), AES.MODE_ECB)
    ciphertext = encobj.encrypt(fix_message(plaintext))
     
    # Resulting ciphertext in hex
    return ciphertext.encode('hex')

def decrypt(key, ciphertext):
    ciphertext = binascii.unhexlify(ciphertext)
     
    decobj = AES.new(fix_key(key), AES.MODE_ECB)
    plaintext = decobj.decrypt(ciphertext)
     
    # Resulting plaintext
    return unfix_message(plaintext)


def fix_key(key):
    """Make sure the key is exactly 16 characters long"""
    key = key[:16]
    while len(key) < 16:
        key += 'a'  # spam a's until it's long enough
    return key

def fix_message(message):
    """pad the string with null characters until
    it's length is a multiple of 16"""

    while len(message) % 16 != 0:
        message += '\0'  # pad with null characters

    return message

def unfix_message(message):
    """remove any null characters from the string"""

    msg = ""
    for c in message:
        if c != '\0':
            msg += c
    return msg

if __name__ == "__main__":

    enc = encrypt('banana', 'Secret Message ')
    print enc
    print "|{}|".format(decrypt('banana', enc))

#    print fix_key("12345678901234567")
#    print fix_key("banana")
#    print len(fix_key("banana"))
#
