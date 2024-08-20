from dronekit import connect, VehicleMode
import time

def arm_and_disarm():
    # Wait for the vehicle to become armable
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable...")
        time.sleep(1)
    print("Vehicle is now armable")

    # Arm the vehicle
    vehicle.mode = VehicleMode("STABILIZE")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for vehicle to become armed...")
        time.sleep(1)
    print("Vehicle is now armed")
    print("WARNING: Props are spinning!")

    # Hold the arm state for a few seconds
    time.sleep(5)

    # Disarm the vehicle
    vehicle.armed = False

    while vehicle.armed:
        print("Waiting for vehicle to disarm...")
        time.sleep(1)
    print("Vehicle is now disarmed")
    print("Props have stopped spinning. It's safe now!")

def connect_my_copter():
    # Connect to the vehicle
    return connect('/dev/ttyACM0', baud=115200, wait_ready=True)

# Main execution
vehicle = connect_my_copter()
arm_and_disarm()

print("End of script.")
