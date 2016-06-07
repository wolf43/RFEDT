"""This module provides a command line tool to decrypt files with a RSA private key."""

# The name RFDT stands for RSA File Decryption Tool
# This is something I wrote when I was trying to understand RSA encryption
# Dependencies: Python 2.7, pycryptodome(http://pycryptodome.readthedocs.io/en/latest/)
import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


# Get file to decrypt
user_encrypted_file = raw_input("\n\nFILE INPUT\nEnter file to decrypt:")
with open(user_encrypted_file, 'rb') as in_file:
    received_msg = pickle.load(in_file)

# received_msg = transmitted_message
print "Received message: " + str(received_msg)
encrypted_session_key, received_aad, received_ciphertext, received_tag, received_nonce = received_msg[0], received_msg[1], received_msg[2], received_msg[3], received_msg[4]

# Get RSA private key
rsa_private_key = raw_input("Enter private key to decrypt with:")
private_key = "rsa_private_key1.pem"
private_key = RSA.import_key(open(rsa_private_key).read())

# Decrypt the session key with the RSA private key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(encrypted_session_key)
print "Decryption Key: " + str(session_key)

# Validate MAC and decrypt
# If MAC validation fails, ValueError exception will be thrown
cipher = AES.new(session_key, AES.MODE_GCM, received_nonce)
cipher.update(received_aad)
try:
    decrypted_data = cipher.decrypt_and_verify(received_ciphertext, received_tag)
    print "\nMAC validated: Data was encrypted with a seesion key that was encrypted with private key used for decryption"
    print "\nAuthenticated AAD: " + str(received_aad)
    # print "Decrypted sensitive data: " + str(decrypted_data)
except ValueError as mac_mismatch:
    print "\nMAC validation failed during decryption. No authentication gurantees on this ciphertext"
    print "\nUnauthenticated AAD: " + str(received_aad)

user_decrypted_file = raw_input("\n\nDECRYPTED FILE NAME\nChoose name for decrypted file:")
output_file_handle = open(user_decrypted_file, 'wb')
output_file_handle.write(decrypted_data)
output_file_handle.close()
