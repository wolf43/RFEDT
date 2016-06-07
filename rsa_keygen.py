"""This module generates a RSA key pair and stores public and private keys in files."""
from Crypto.PublicKey import RSA

# Generate RSA key pair
key = RSA.generate(2048)


# Get name of private key from user
default_private_key_name = "rsa_private_key.pem"
user_private_key_name = raw_input("NAME FOR FILE WHERE GENERATED RSA PRIVATE KEY SHOULD BE STORED\nDefault: " + str(default_private_key_name) + "\nEnter name for file where generated private key should be stored:")
private_key_name = user_private_key_name or default_private_key_name

# Write the RSA key to a file
private_key = key.exportKey()
file_out = open(private_key_name, "wb")
file_out.write(private_key)


# Get name of public key file
default_public_key_name = "rsa_public_key.pem"
user_public_key_name = raw_input("NAME FOR FILE WHERE GENERATED RSA PUBLIC KEY SHOULD BE STORED\nDefault: " + str(default_public_key_name) + "\nEnter name for file where generated public key should be stored:")
public_key = user_public_key_name or default_public_key_name

# Write public key of RSA key pair to a file
file_out = open(public_key, "wb")
public_key = key.publickey().exportKey()
file_out.write(public_key)
