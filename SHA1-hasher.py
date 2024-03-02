import hashlib

password = input("Password To Hash: ")

hashed_password = hashlib.sha1(password.encode()).hexdigest()

print("Hashed Password (SHA-1):", hashed_password)
