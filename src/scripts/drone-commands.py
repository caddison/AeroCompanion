# drone_commands.py
from vehicle_connect import vehicle

def move_drone(command: str):
    if vehicle is None:
        print("Vehicle not connected")
        return
    
    if command == 'Move Up':
        vehicle.simple_takeoff(vehicle.location.global_relative_frame.alt + 1)
    elif command == 'Move Down':
        vehicle.simple_takeoff(vehicle.location.global_relative_frame.alt - 1)
    elif command == 'Move Forward':
        move_forward(vehicle)
    elif command == 'Move Backward':
        move_backward(vehicle)
    elif command == 'Pan Left':
        pan_left(vehicle)
    elif command == 'Pan Right':
        pan_right(vehicle)
    elif command == 'Roll Left':
        roll_left(vehicle)
    elif command == 'Roll Right':
        roll_right(vehicle)

def move_forward(vehicle):
    vehicle.channels.overrides['2'] = 1600  # Pitch forward

def move_backward(vehicle):
    vehicle.channels.overrides['2'] = 1400  # Pitch backward

def pan_left(vehicle):
    vehicle.channels.overrides['4'] = 1400  # Yaw left

def pan_right(vehicle):
    vehicle.channels.overrides['4'] = 1600  # Yaw right

def roll_left(vehicle):
    vehicle.channels.overrides['1'] = 1400  # Roll left

def roll_right(vehicle):
    vehicle.channels.overrides['1'] = 1600  # Roll right

def reset_overrides():
    if vehicle is not None:
        vehicle.channels.overrides = {}

def execute_command(command: str):
    move_drone(command)
    reset_overrides()

if __name__ == '__main__':
    # Example command execution
    commandString = 'Move Forward'  # This would come from your joystick input logic
    execute_command(commandString)
