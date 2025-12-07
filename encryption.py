# encryption.py

from cryptography.fernet import Fernet
import base64
import hashlib
import os

# Function to generate a key from a user-provided password
def generate_key(password: str) -> bytes:
    """Generates a Fernet key from a password using SHA-256."""
    # Hash the password to create a 32-byte key
    key_bytes = hashlib.sha256(password.encode()).digest()
    # Fernet requires the key to be URL-safe base64 encoded
    return base64.urlsafe_b64encode(key_bytes)

def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypts data using a password."""
    key = generate_key(password)
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_data(token: bytes, password: str) -> bytes:
    """Decrypts data using a password."""
    key = generate_key(password)
    f = Fernet(key)
    # The Fernet object will raise an InvalidToken exception if the password is wrong
    return f.decrypt(token)

def is_encrypted_file(file_path: str) -> bool:
    """Checks if a file starts with the Fernet magic header (b'gAAAAA')."""
    try:
        with open(file_path, 'rb') as f:
            header = f.read(6)
        # Fernet tokens usually start with a specific sequence after base64 encoding
        return header.startswith(b'gAAAAA')
    except:
        return False