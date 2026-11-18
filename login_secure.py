import hashlib

pwd = 'secure password'
hashed = hashlib.sha256(pwd.encode().hexdigest())
print(hashed.hexdigest())

Input_password = input()
Input_hashed = hashed = hashlib.sha256(Input_password.encode().hexdigest())

if(hashed == Input_hashed):
    print("login success")