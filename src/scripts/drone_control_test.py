import sys
import base64
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Util.Padding import unpad
from drone_commands import execute_command

# Use the temporary key "key" and hash it to 32 bytes
secure_key = "key"
hashed_key = SHA256.new(data=secure_key.encode('utf-8')).digest()

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
        print(f"Calculated HMAC (Hex): {calculated_hmac}")  # Log for comparison

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

# Function to execute the drone command
def handle_command(command):
    print(f"Command received: {command}")

    # Mapping of the decrypted command to drone functions
    command_mapping = {
        'Move Up': 'Move Up',
        'Move Down': 'Move Down',
        'Move Forward': 'Move Forward',
        'Move Backward': 'Move Backward',
        'Pan Left': 'Pan Left',
        'Pan Right': 'Pan Right',
        'Roll Left': 'Roll Left',
        'Roll Right': 'Roll Right',
        'Video Stream On': 'Video Stream On',
        'Video Stream Off': 'Video Stream Off',
        'Voice Record On': 'Voice Record On',
        'Voice Record Off': 'Voice Record Off',
        'Land': 'Land'  
    }

    # Execute the command if it exists in the mapping
    if command in command_mapping:
        execute_command(command_mapping[command])
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python drone_control_test.py <encrypted_command_with_hmac>")
        sys.exit(1)

    encrypted_command_with_hmac = sys.argv[1]

    try:
        # Decrypt the received message
        decrypted_command = decrypt_message(encrypted_command_with_hmac, hashed_key)
        # Handle the decrypted command
        handle_command(encrypted_command_with_hmac)
    except ValueError as ve:
        print(f"Error: {ve}")
