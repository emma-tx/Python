#Encrypt text with PyCrypto XOR module
#Michael, January 2014

import os
import string
import base64
import binascii
import hashlib
from Crypto.Cipher import XOR

message = raw_input('MESSAGE: ')
msg2 = base64.b64encode(message)

userPass = raw_input('KEY: ')

obj1 = XOR.new(userPass)
ciphertext = obj1.encrypt(msg2)
print ('CIPHERTEXT: ')
print ciphertext
