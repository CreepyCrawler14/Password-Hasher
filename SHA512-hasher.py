import hashlib

password = input("Password To Hash: ")

hashed_password = hashlib.sha512(password.encode()).hexdigest()

print("Hashed Password (SHA-512):", hashed_password)
