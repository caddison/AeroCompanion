from vehicle_connect import vehicle
from dronekit import VehicleMode

def move_drone(command: str):
    if vehicle is None:
        print("Vehicle not connected")
        return
    
    if command == 'Move Up':
        move_up(vehicle)
    elif command == 'Move Down':
        move_down(vehicle)
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

def move_up(vehicle):
    # Increase altitude by 1 meter
    new_altitude = vehicle.location.global_relative_frame.alt + 1
    vehicle.simple_goto(vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, new_altitude)

def move_down(vehicle):
    # Decrease altitude by 1 meter, ensuring it doesn't go below 0
    new_altitude = max(0, vehicle.location.global_relative_frame.alt - 1)
    vehicle.simple_goto(vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, new_altitude)

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
