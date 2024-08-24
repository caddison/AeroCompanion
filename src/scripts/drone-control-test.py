import sys
import base64
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Util.Padding import unpad

# Secure key (replace this with the actual key used in your JavaScript code)
secure_key = "key"  # Original key

# Derive a 256-bit key (32 bytes) using SHA-256
hash_object = SHA256.new(data=secure_key.encode('utf-8'))
key = hash_object.digest()  # This gives a 32-byte key

def decrypt_message(encrypted_message_with_hmac, key):
    try:
        # Split the encrypted message and the HMAC
        encrypted_message, received_hmac = encrypted_message_with_hmac.split('|')

        # Decode the base64 encoded encrypted message
        encrypted_message_bytes = base64.b64decode(encrypted_message)
        print(f"Base64-decoded message: {encrypted_message_bytes.hex()}")

        # Extract the IV and ciphertext
        iv = encrypted_message_bytes[:16]
        ciphertext = encrypted_message_bytes[16:]

        print(f"IV: {iv.hex()}")
        print(f"Ciphertext: {ciphertext.hex()}")

        # Verify HMAC
        hmac = HMAC.new(key, msg=encrypted_message_bytes, digestmod=SHA256)
        calculated_hmac = hmac.hexdigest()

        if calculated_hmac != received_hmac:
            print(f"Received HMAC: {received_hmac}")
            print(f"Calculated HMAC: {calculated_hmac}")
            raise ValueError("HMAC verification failed.")

        # Create the cipher object and decrypt the data
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')

        return decrypted_message

    except ValueError as ve:
        raise ValueError(f"Decryption failed: {ve}")
    except Exception as e:
        raise ValueError(f"Unexpected error during decryption: {e}")

# Function to print the received command
def handle_command(command):
    print(f"Command received: {command}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python drone_control_test.py <encrypted_command_with_hmac>")
        sys.exit(1)

    encrypted_command_with_hmac = sys.argv[1]

    try:
        # Decrypt the received message
        decrypted_command = decrypt_message(encrypted_command_with_hmac, key)
        handle_command(decrypted_command)
    except ValueError as e:
        print(f"Decryption failed: {e}")
