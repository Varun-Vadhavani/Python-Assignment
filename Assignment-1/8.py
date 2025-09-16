import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {
    "admin" : hash_password("12345"),
    "varun" : hash_password("67890")
}

username = input("Enter username: ")
if username not in users:
    print("Invalid Username")
else:
    password = input("Enter password: ")
    entered_hashed = hash_password(password)
    if(entered_hashed == users[username]):
        print("Login Successful!")
    else:
        print("Invalid Password")