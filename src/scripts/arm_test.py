from dronekit import connect, VehicleMode
import time
import logging

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

def disable_all_checks(vehicle):
    try:
        print("Disabling all pre-arm checks and safety mechanisms...")
        
        # Disable pre-arm checks
        vehicle.parameters['ARMING_CHECK'] = 0
        
        # Disable GPS-related checks (if any)
        vehicle.parameters['GPS_TYPE'] = 0
        
        # Disable geofence
        vehicle.parameters['FENCE_ENABLE'] = 0
        
        # Set throttle failsafe to disabled
        vehicle.parameters['FS_THR_ENABLE'] = 0
        
        # Disable battery failsafe
        vehicle.parameters['FS_BATT_ENABLE'] = 0
        
        # Disable radio failsafe
        vehicle.parameters['FS_GCS_ENABLE'] = 0
        
        print("All checks and safety features disabled.")
    except Exception as e:
        print(f"Error disabling checks: {e}")

def main():
    # List of potential serial devices
    devices = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyUSB2', '/dev/ttyUSB3']

    vehicle = None
    for device in devices:
        try:
            print(f"Trying to connect to {device}")
            vehicle = connect(device, baud=115200, wait_ready=True, heartbeat_timeout=60)
            print(f"Connected to vehicle on {device}")
            break
        except Exception as e:
            print(f"Failed to connect to {device}: {e}")
    
    if not vehicle:
        print("Unable to connect to any devices. Exiting.")
        return

    # Disable all pre-arm checks and failsafes
    disable_all_checks(vehicle)

    # Wait for the vehicle to be ready
    vehicle.wait_ready('autopilot_version', 'parameters', timeout=60)
    print("Connected and ready.")

    # Set the vehicle mode to STABILIZE or ALT_HOLD (since these do not require GPS)
    print("Setting vehicle mode to STABILIZE...")
    vehicle.mode = VehicleMode("STABILIZE")
    while not vehicle.mode.name == "STABILIZE":
        print(f"Waiting for mode change... Current mode: {vehicle.mode.name}")
        time.sleep(1)
    print("Vehicle mode set to STABILIZE.")

    # Arm the vehicle
    print("Arming the vehicle...")
    vehicle.armed = True
    while not vehicle.armed:
        print("Waiting for vehicle to arm...")
        time.sleep(1)
    print("Vehicle is armed.")

    # Wait for a few seconds
    print("Vehicle is now armed. Waiting for 5 seconds...")
    time.sleep(5)

    # Disarm the vehicle
    print("Disarming the vehicle...")
    vehicle.armed = False
    while vehicle.armed:
        print("Waiting for vehicle to disarm...")
        time.sleep(1)
    print("Vehicle is disarmed.")

    # Close vehicle object
    vehicle.close()
    print("Vehicle connection closed.")

if __name__ == "__main__":
    main()

