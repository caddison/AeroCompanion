import sys
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Use the temporary key "key"
secure_key = "key"

def decrypt_message(encrypted_message, key):
    try:
        # Decode the base64 encoded encrypted message
        encrypted_message_bytes = base64.b64decode(encrypted_message)
        print(f"Base64-decoded message: {encrypted_message_bytes.hex()}")

        # Extract the IV and ciphertext
        iv = encrypted_message_bytes[:16]
        ciphertext = encrypted_message_bytes[16:]

        print(f"IV: {iv.hex()}")
        print(f"Ciphertext: {ciphertext.hex()}")

        # Create the cipher object and decrypt the data
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
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
        print("Usage: python drone_control_test.py <encrypted_command>")
        sys.exit(1)

    encrypted_command = sys.argv[1]

    try:
        # Decrypt the received message
        decrypted_command = decrypt_message(encrypted_command, secure_key)
        handle_command(decrypted_command)
    except ValueError as e:
        print(f"Decryption failed: {e}")
