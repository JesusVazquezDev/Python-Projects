More Password Cracking
> **University Project:** Extra Credit in HW2 for CS642-Information Security

Yet another colleague, to make the password cracking hard, uses a **slow hash function** named `scrypt`. 

**Scrypt** is a password-based key derivation function that is designed to be computationally intensive (slow).
This is because legitimate users only need to perform the function once per operation (e.g., during authentication), and so the computational overhead and the time required is not noticeable.
However, a brute-force attacker would likely need to perform the operation billions of times, at which point the time computational requirements become significant and, ideally, prohibitive.

For example, the input `batman,password`, and salt `84829348943` processed with scrypt produces the following hash:
`594b32011f597e921b07be213b469a94492ddcdeea84ffea27e2e0392e77f6c59690f1f85b22b8fcb9f551f6613880ef1dc1cc855d600165b8a285c9a342ad8f`

While using the same technique, for the username `bucky` with salt `9578721033` (and also keeping n = `16`, r = `32`, p = `1`) the challenge hash is
`80cb3696e6fe9953e61048ad0013e4e9d31e26d0b10eec5650b26625033dfbe4203f1cc793e2df9031e96a1a877cce2f5da4cc8ec0698c382438aae4591a5d1a`

The password is representative of real-world passwords: 
something complex enough that the person that selected this password would consider using it for a website login, but easy enough to be memorable. 

Tasks:

1. Find the password used to produce the challenge hash. 
  - Give a pseudocode description of your algorithm and the correct password in `solutions.txt`.

> Hints for Extra Credit:
The website has a password policy that requires that the password must have at **least 6 characters and at least three of the four character classes: uppercase letters (A-Z), lower case letters (a-z), symbols (`~!@#$%^&*()+=_-{}[]\|:;”’?/<>,.), and digits (0-9)**.

You can look at CrackStation's password cracking dictionaries for some help.

Note: the password is **human-chosen**, so you should use the smaller "human password" dataset.
It is wise to estimate the running time of your solution before starting it.
