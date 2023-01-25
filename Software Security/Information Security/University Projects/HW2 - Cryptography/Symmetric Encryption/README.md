# Symmetric & Asymmetric Encryption

> **University Project:** Part B of HW2 for CS642-Information Security

A colleague decided to build a symmetric encryption scheme. 

This is implemented in `badencrypt.py` and `baddecrypt.py`.

These are specifically designed to encrypt **a sample message** to demonstrate the encryption scheme.

To use these demo programs, run:
```
  CT=$(python3 badencrypt.py testkeyfile)
  echo $CT
  python3 baddecrypt.py testkeyfile $CT
```

You are tasked with assessing the security of this encryption scheme.

Your solution will be a Python program `attack.py` which takes a *ciphertext* as input and modifies the ciphertext so the decrypted message has a different (and more lucrative to the recipient) **TOTAL** field and still passes the verification in `baddecrypt.py`.

**The file `attack.py` must do this without access to the key file or knowledge of the key.**

You can assume the ciphertext contains the sample message hardcoded in `badencrypt.py`.

We will test your solution with original versions of badencrypt.py and baddecrypt.py and with different encryption keys than the test key provided.

To ensure that `attack.py` produces the correct formatted output, you can run from the command line:
```
 CT=$(python3 badencrypt.py testkeyfile) 
 MODCT=$(python3 attack.py $CT) 
 python3 baddecrypt.py testkeyfile $MODCT
```
Tasks:
1. Complete the attack program `attack.py`
2. In `solutions.txt`, **describe** what is wrong with your colleague's scheme and how it should be fixed so that it will be more secure.

**(Your attack script will not have direct access to the key file and should not attempt to gain access to the process memory of baddecrypt or any other files to steal the key directly.)**
