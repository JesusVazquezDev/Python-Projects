# code for Part A
import sys
from itertools import product
import hashlib




# parse the correct hash value, username, and salt
[program, correctHash, username, salt] = sys.argv

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# guess all possible passwords up to 8 digits
for i in range(1, 9):
    # generate all password with i digits
    for password in product(digits, repeat=i):
        passwordGuess  = ''.join(password)
        # hash the password and compare to correct hash
        guessString = username + "," + passwordGuess + "," + salt
        guessHash = hashlib.sha256(guessString.encode()).hexdigest()
        if guessHash == correctHash:
            print("User password: " + passwordGuess)
            exit()





