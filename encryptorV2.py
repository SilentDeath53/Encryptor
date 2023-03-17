from Cryptodome.Cipher import AES
import os

key = 'your_key'

input_file = 'path/to/file'
output_file = 'path/to/new/file'

cipher= AES.new(key, AES.MODE_EAX)

with open (input_file, 'rb') as f:
    data = f.read()

ciphertext, tag = cipher.encrypt_and_digest(data)

with open(output_file, 'wb') as f:
    [f.write(x) for x in (cipher.nonce, tag, ciphertext)]
