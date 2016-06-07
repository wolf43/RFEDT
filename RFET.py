"""This module provides a command line tool to encrypt files with a RSA public key."""

# The name RFET stands for RSA File Encryption Tool
# This is something I wrote when I was trying to understand RSA encryption
# Dependencies: Python 2.7, pycryptodome(http://pycryptodome.readthedocs.io/en/latest/)
import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Authenticated encryption on a string using AES GCM with both encryption and MAC

# Public key input
public_key = raw_input("RSA PUBLIC KEY INPUT\nEnter file that has the pulic key:")
# public_key = "rsa_public_key1.pem"
recipient_key = RSA.import_key(open(public_key).read())
session_key = get_random_bytes(16)
print "AES Encryption Key: " + str(session_key)
cipher_rsa = PKCS1_OAEP.new(recipient_key)
encrypted_session_key = cipher_rsa.encrypt(session_key)
print "Encrypted session key: " + str(encrypted_session_key)

# Sensitive file to encrypt
user_sensitive_file = raw_input("\n\nFILE INPUT\nEnter file to encrypt:")
input_file_handle = open(user_sensitive_file, 'rb')
sensitive_data = input_file_handle.read()
input_file_handle.close()
print "Sensitive data encrypted: " + str(sensitive_data)

# Additional data to authenticate - won't be encrypted but will be authenticated
default_aad = ""
user_aad = raw_input("\n\nAAD INPUT\nThis won't be encrypted but it will be authenticated\nDefault: " + str(default_aad) + "\nEnter associated authenticated data:")
aad = user_aad or default_aad
print "Associated authenticated data: " + str(aad)

# Encrypt using AES GCM
cipher = AES.new(session_key, AES.MODE_GCM)
cipher.update(aad)
ciphertext, tag = cipher.encrypt_and_digest(sensitive_data)
# Nonce is generated randomly if not provided explicitly
nonce = cipher.nonce

# Message to transmit/share
transmitted_message = [encrypted_session_key, aad, ciphertext, tag, nonce]
print "\nTransmitted message: " + str(transmitted_message)
print "Type: " + str(type(transmitted_message))


# Saving message in a file
default_output_filename = "encrypted_file.enc"
user_output_filename = raw_input("\n\nOUTPUT FILENAME INPUT\nDefault: " + str(default_output_filename) + "\nEnter output filename:")
output_filename = user_output_filename or default_output_filename
with open(output_filename, 'wb') as out_file:
    pickle.dump(transmitted_message, out_file)
print "Encrypted output filename: " + str(output_filename)
