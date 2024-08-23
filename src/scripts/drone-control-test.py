import sys
import base64
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad

# Secure key (replace this with the actual key used in your JavaScript code)
secure_key = "key"  # Must match the key used in JavaScript

def decrypt_message(encrypted_message, key):
    # Decode the base64 encoded message
    encrypted_message = base64.b64decode(encrypted_message)
    
    # Extract the IV and ciphertext
    iv = encrypted_message[:16]
    ciphertext = encrypted_message[16:-32]  # Assuming the last 32 bytes are the HMAC SHA256 hash
    received_hmac = encrypted_message[-32:]
    
    # Create the cipher object and decrypt the data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    
    # Verify HMAC
    hmac = HMAC.new(key, msg=encrypted_message[:-32], digestmod=SHA256)
    if hmac.digest() != received_hmac:
        raise ValueError("HMAC verification failed.")
    
    return decrypted_message

# Function to print the received command
def handle_command(command):
    print(f"Command received: {command}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python drone_control_test.py <encrypted_command>")
        sys.exit(1)
    
    encrypted_command = sys.argv[1]
    
    # Convert secure key from hex string to bytes
    key = bytes.fromhex(secure_key)
    
    try:
        # Decrypt the received message
        decrypted_command = decrypt_message(encrypted_command, key)
        handle_command(decrypted_command)
    except ValueError as e:
        print(f"Decryption failed: {e}")
