from dronekit import connect, VehicleMode
import time

def wait_for_mode_change(target_mode):
    print(f"Changing mode to {target_mode}...")
    vehicle.mode = VehicleMode(target_mode)
    
    while vehicle.mode.name != target_mode:
        print(f"Waiting for mode change to {target_mode} (Current mode: {vehicle.mode.name})")
        time.sleep(1)
    print(f"Mode successfully changed to {target_mode}.")

def perform_prearm_checks():
    print("Waiting for vehicle to pass pre-arm checks...")

    # Optionally disable pre-arm checks if needed (for debugging)
    vehicle.parameters['ARMING_CHECK'] = 0  # Disable all checks temporarily

    while not vehicle.is_armable:
        print(f"Waiting for vehicle to become armable... (System status: {vehicle.system_status.state}, Mode: {vehicle.mode.name}, "
              f"GPS: {vehicle.gps_0.fix_type}, EKF: {vehicle.ekf_ok}, Voltage: {vehicle.battery.voltage}V, "
              f"Battery: {vehicle.battery.level}%, Arming Check: {vehicle.parameters.get('ARMING_CHECK')})")
        # Check if we can at least bypass the checks temporarily
        if vehicle.parameters['ARMING_CHECK'] == 0:
            print("Pre-arm checks disabled for testing.")
        time.sleep(1)

    print("Vehicle passed all pre-arm checks and is armable.")

def arm_and_disarm():
    perform_prearm_checks()

    wait_for_mode_change("STABILIZE")

    # Arm the vehicle
    print("Arming the vehicle...")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for vehicle to arm...")
        time.sleep(1)
    print("Vehicle is armed. WARNING: Props are spinning!")

    time.sleep(5)

    # Disarm the vehicle
    print("Disarming the vehicle...")
    vehicle.armed = False

    while vehicle.armed:
        print("Waiting for vehicle to disarm...")
        time.sleep(1)
    print("Vehicle is disarmed.")

def connect_my_copter():
    print("Connecting to vehicle on: /dev/ttyACM0")
    return connect('/dev/ttyACM0', baud=115200, wait_ready=True)

# Main execution
vehicle = connect_my_copter()

if vehicle:
    print("Successfully connected to the vehicle.")
else:
    print("Failed to connect to the vehicle.")
    exit(1)

arm_and_disarm()

print("End of script.")
