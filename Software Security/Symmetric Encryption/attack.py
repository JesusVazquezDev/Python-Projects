# /usr/bin/env python3

# CS 642 University of Wisconsin
#
# usage: python3 attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys
import hashlib

def xor_func(input1, input2):
  return bytes(a ^ b for a, b in zip(input1, input2))

# Grab ciphertext from first argument
ciphertextWithTag = bytes.fromhex(sys.argv[1])

if len(ciphertextWithTag) < 16+16+32:
  print("Ciphertext is too short!")
  sys.exit(0)


iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[:len(ciphertextWithTag)-32]
tag = ciphertextWithTag[len(ciphertextWithTag)-32:]

# TODO: Modify the input so the transfer amount is more lucrative to the recipient

message = \
"""TOTAL:  $  15.99
Originating Acct Holder: Alexa
Orgininating Acct #98166-20633

I authorized the above amount to be transferred to the account #51779-31226 
held by a Wisc student at the National Bank of the Cayman Islands.
"""

mal_message = \
"""TOTAL:  $  99.99
Originating Acct Holder: Alexa
Orgininating Acct #98166-20633

I authorized the above amount to be transferred to the account #51779-31226 
held by a Wisc student at the National Bank of the Cayman Islands.
"""

message_encoded = message.encode()
mal_message_encoded = mal_message.encode()

# E = original plain text ^ original IV
E  = xor_func(message_encoded, iv)
# malIV =  E ^ mal plain text
malIV = xor_func(E, mal_message_encoded)
# new tag
tag = hashlib.sha256(mal_message_encoded).hexdigest()

# TODO: Print the new encrypted message
# you can change the print content if necessary
print(malIV.hex() + ciphertext[16:].hex() + tag)

