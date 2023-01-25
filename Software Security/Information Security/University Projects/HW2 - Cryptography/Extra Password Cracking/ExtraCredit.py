import hashlib
import sys

username = "bucky";

salting = "9578721033";

challenge_hash = '80cb3696e6fe9953e61048ad0013e4e9d31e26d0b10eec5650b26625033dfbe4203f1cc793e2df9031e96a1a877cce2f5da4cc8ec0698c382438aae4591a5d1a'

def comb1(password): # A-Z 		a-z	 	0-9
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            if any(char.islower() for char in password):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
def comb2(password): # a-z 	Punc 	0-9
    if any(char.isdigit() for char in password):
        if(any(char.islower() for char in password)):
            if(any(char.isprintable() for char in password)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
def comb3(password): # A-Z 		a-z 		Punc
    if any(char.isupper() for char in password):
        if(any(char.islower() for char in password)):
            if(any(char.isprintable() for char in password)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
def comb4(password): # A-Z 	Punc 	0-9
    if any(char.isdigit() for char in password):
        if(any(char.isupper() for char in password)):
            if(any(char.isprintable() for char in password)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Basic Input

f = open(sys.argv[1], 'r', encoding=('latin-1'))
password_list = f.readlines()
invalid_list = []
f.close()


for passwordF in password_list: 
    passwordF = passwordF.strip()
    if(len(passwordF) >= 6):
        if(comb1(passwordF) == True):
            message = username + "," + passwordF
            print(f'Processed1 {message}')
            found = hashlib.scrypt (password=message.encode(), salt = salting.encode(), n = 16, r = 32, p = 1)
            if(found.hex() == challenge_hash):
                print(f'FOUND! Password is {passwordF}')
                break
        elif(comb2(passwordF) == True):
            message = username + "," + passwordF
            print(f'Processed2 {message}')
            found = hashlib.scrypt (password=message.encode(), salt = salting.encode(), n = 16, r = 32, p = 1)
            if(found.hex() == challenge_hash):
                print(f'FOUND! Password is {passwordF}')
                break
        elif(comb3(passwordF) == True):
            message = username + "," + passwordF
            print(f'Processed3 {message}')
            found = hashlib.scrypt (password=message.encode(), salt = salting.encode(), n = 16, r = 32, p = 1)
            if(found.hex() == challenge_hash):
                print(f'FOUND! Password is {passwordF}')
                break
        elif(comb4(passwordF) == True):
            message = username + "," + passwordF
            print(f'Processed4 {message}')
            found = hashlib.scrypt (password=message.encode(), salt = salting.encode(), n = 16, r = 32, p = 1)
            if(found.hex() == challenge_hash):
                print(f'FOUND! Password is {passwordF}')
                sys.exit(0)
        else:
            print(f'INVALID PASSWORD {passwordF}')
            invalid_list.append(passwordF)
        
print("COMPLETED")
