import hashlib

password = input("Password To Hash: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Hashed Password (SHA-256):", hashed_password)
