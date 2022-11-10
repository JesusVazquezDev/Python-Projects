import hashlib

username1 = "bjacobsen";
username2 = "ceccio";

salt1 = "55570237";
salt2 = "33181065";

key1 = "995345e92d5d62c7439a99bc5422d0caa2737583ebef0f4bedf81bd9a730181f"
key2 = "c444a02be670bec7401c11fed91302dcc284136338be419866f085717aa18b7f"


i = 0
found1 = False
found2 = False

while(i < pow(10,8)):
    find1 = username1  + "," + str(i).zfill(8) + "," + salt1
    find2 = username2  + "," + str(i).zfill(8) + "," + salt2
    
    if (hashlib.sha256(find1.encode()).hexdigest() == key1):
        print(f'Password for User1: {str(i).zfill(8)}')
        found1 = True

    if (hashlib.sha256(find2.encode()).hexdigest() == key2):
        print(f'Password for User2: {str(i).zfill(8)}')
        found2 = True
        
    if(found1 == True and found2 == True):
        break
    
    i+=1

print("COMPLETED")
