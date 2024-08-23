import sys

# Function to print the received command
def handle_command(command):
    print(f"Command received: {command}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python drone_control_test.py <command>")
        sys.exit(1)

    command = sys.argv[1]
    handle_command(command)
