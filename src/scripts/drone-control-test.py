import socket
from dronekit import connect

# Connect to the drone 
vehicle = connect('/dev/ttyACM0', baud=115200, wait_ready=True)

# Function to interpret commands and control the drone
def handle_command(command):
    if command == 'Move Up':
        vehicle.channels.overrides['3'] = 1700  # Throttle up
    elif command == 'Move Down':
        vehicle.channels.overrides['3'] = 1300  # Throttle down
    elif command == 'Move Forward':
        vehicle.channels.overrides['2'] = 1600  # Pitch forward
    elif command == 'Move Backward':
        vehicle.channels.overrides['2'] = 1400  # Pitch backward
    elif command == 'Pan Left':
        vehicle.channels.overrides['4'] = 1300  # Yaw left
    elif command == 'Pan Right':
        vehicle.channels.overrides['4'] = 1700  # Yaw right
    elif command == 'Roll Left':
        vehicle.channels.overrides['1'] = 1300  # Roll left
    elif command == 'Roll Right':
        vehicle.channels.overrides['1'] = 1700  # Roll right
    else:
        print(f"Unknown command: {command}")

# Set up UDP server to listen for commands from Node.js
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Bind to all network interfaces
    sock.bind(('0.0.0.0', 14551))
    print("Listening for commands on port 14551...")
except socket.error as e:
    print(f"Socket error: {e}")
    sock.close()
    exit(1)

while True:
    try:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        if data:
            command = data.decode('utf-8')
            print(f"Received command from {addr}: {command}")
            handle_command(command)
        else:
            print(f"Received empty data from {addr}")
    except socket.error as e:
        print(f"Socket error while receiving data: {e}")
