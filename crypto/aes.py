# NEVER USE ECB is not secure

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16) # 16 bytes -> 128 bits: AES-128

aesCipher = Cipher(algorithms.AES(key),modes.ECB(), backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()
