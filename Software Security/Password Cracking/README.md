# Password Cracking 
> ( Part A of HW2 in CS642-Information Security )

A colleague has built a password hashing mechanism.
It applies SHA-256 to a string of the form `"username,password,salt"`, where salt is a randomly chosen value.

EX: The stored value for username `user`, password `12345` and salt `999999` is `c50603be4fedef7a260ef9181a605c27d44fe0f37b3a8c7e8dbe63b9515b8e96`.

The Python code to generate this is:

```
import hashlib
print(hashlib.sha256("user,12345,999999".encode()).hexdigest())
```

The same process was used to generate the following challenge hashes: 

a) `995345e92d5d62c7439a99bc5422d0caa2737583ebef0f4bedf81bd9a730181f` for user `bjacobsen` and salt `55570237`.

b) `c444a02be670bec7401c11fed91302dcc284136338be419866f085717aa18b7f` for user `ceccio` and salt `33181065`.

Tasks:

- Recover the password for both challenge hashes above.
  - Hint: Both the passwords are an ASCII string consisting only of numeric digits up to 8 digits.
- Give a pseudocode description of your algorithm and the worst-case running time for it.
- Discuss the merits of your colleague’s proposal. Suggest how your attack might be made *intractable*.
- Put your solutions under the correct section in the file `solutions.txt`.
- Upload the `pwcrack.py` containing the code to crack the hashes, with **clear instructions** about how to run it.
