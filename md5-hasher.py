import hashlib

password = input("Password To Hash: ")

hashed_password = hashlib.md5(password.encode()).hexdigest()

print("Hashed Password (MD5):", hashed_password)
