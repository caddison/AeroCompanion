import time
from drone_connect_test import vehicle
from dronekit import VehicleMode

# Global variables to store the last command time and last command received
last_command_time = 0
command_interval = 0.5  # Interval in seconds between command executions
last_command = None

def move_drone(command: str):
    global last_command_time, last_command

    if vehicle is None:
        print("Vehicle not connected")
        return
    
    current_time = time.time()
    
    # Check if the command is the same as the last command and if the interval has passed
    if command == last_command and (current_time - last_command_time) < command_interval:
        print(f"Ignoring command {command} due to debounce interval.")
        return
    
    # Update the last command time and last command
    last_command_time = current_time
    last_command = command
    
    # Execute the corresponding movement command
    if command == 'Move Up':
        gradual_move(vehicle, '3', 1600)  # Throttle up
    elif command == 'Move Down':
        gradual_move(vehicle, '3', 1400)  # Throttle down
    elif command == 'Move Forward':
        gradual_move(vehicle, '2', 1600)  # Pitch forward
    elif command == 'Move Backward':
        gradual_move(vehicle, '2', 1400)  # Pitch backward
    elif command == 'Pan Left':
        gradual_move(vehicle, '4', 1400)  # Yaw left
    elif command == 'Pan Right':
        gradual_move(vehicle, '4', 1600)  # Yaw right
    elif command == 'Roll Left':
        gradual_move(vehicle, '1', 1400)  # Roll left
    elif command == 'Roll Right':
        gradual_move(vehicle, '1', 1600)  # Roll right
    elif command == 'Land':
        land_drone()  # Initiate landing sequence

def gradual_move(vehicle, channel, target_pwm, step=10, delay=0.05):
    """Gradually move the drone by adjusting the PWM value in steps."""
    current_pwm = vehicle.channels[channel]
    
    while current_pwm != target_pwm:
        if target_pwm > current_pwm:
            current_pwm = min(target_pwm, current_pwm + step)
        else:
            current_pwm = max(target_pwm, current_pwm - step)
        
        vehicle.channels.overrides[channel] = current_pwm
        print(f"Moving on channel {channel} to PWM: {current_pwm}")
        time.sleep(delay)

    print(f"Target PWM {target_pwm} reached on channel {channel}")

def land_drone():
    """Initiate the landing sequence."""
    print("Landing initiated")
    vehicle.mode = VehicleMode("LAND")
    while vehicle.armed:
        print("Waiting for the drone to land...")
        time.sleep(1)
    print("Drone has landed and disarmed.")

def reset_overrides():
    if vehicle is not None:
        vehicle.channels.overrides = {}
    print("Resetting channel overrides")

def execute_command(command: str):
    move_drone(command)
    reset_overrides()

if __name__ == '__main__':
    # Example command execution
    commandString = 'Move Forward'  # This would come from your joystick input logic
    execute_command(commandString)
