# RSA file encryption and decryption tool
### Description
This module provides one python script to generate a RSA key pair and two python scipts for encryption and decryption of files using RSA public and private key. The session is actually encypted with RSA public key. The session key used to encrypt the file using AES in GCM mode    
<https://en.wikipedia.org/wiki/Galois/Counter_Mode>  
### How to run

#### Install dependencies
It requires Python and Pycryptodome<http://pycryptodome.readthedocs.io/en/latest/src/introduction.html>  
You can get Pycryptodome by running "pip install pycryptodome"  
You should do it in a virtual enviorment if you already have pycrypto as it is a fork of pycrypto and they might interfeare with each other in unexpted ways

### RSA key pair generation
* Download the files
* From terminal, run "python rsa_keygen.py"

#### Encryption step
* From terminal, run "python RFET.py"
* It will guide you through the process
* You have to use the public key corresponding to the private key that will be used to decrypt

#### Decryption step
* From terminal, run "python RFDT.py"
* It will guide you through the process
