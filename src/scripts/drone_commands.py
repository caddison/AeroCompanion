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
    new_altitude = vehicle.location.global_relative_frame.alt + 1
    vehicle.simple_goto(vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, new_altitude)
    print(f"Executing command: Move Up. New altitude: {new_altitude} meters")

def move_down(vehicle):
    new_altitude = max(0, vehicle.location.global_relative_frame.alt - 1)
    vehicle.simple_goto(vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, new_altitude)
    print(f"Executing command: Move Down. New altitude: {new_altitude} meters")

def move_forward(vehicle):
    vehicle.channels.overrides['2'] = 1600  # Pitch forward
    print("Executing command: Move Forward")

def move_backward(vehicle):
    vehicle.channels.overrides['2'] = 1400  # Pitch backward
    print("Executing command: Move Backward")

def pan_left(vehicle):
    vehicle.channels.overrides['4'] = 1400  # Yaw left
    print("Executing command: Pan Left")

def pan_right(vehicle):
    vehicle.channels.overrides['4'] = 1600  # Yaw right
    print("Executing command: Pan Right")

def roll_left(vehicle):
    vehicle.channels.overrides['1'] = 1400  # Roll left
    print("Executing command: Roll Left")

def roll_right(vehicle):
    vehicle.channels.overrides['1'] = 1600  # Roll right
    print("Executing command: Roll Right")

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
