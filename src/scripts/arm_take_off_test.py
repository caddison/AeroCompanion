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

def arm_and_takeoff_nogps(vehicle, target_altitude):
    """
    Arms the drone and takes off to a specified altitude using non-GPS modes.
    """
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable...")
        time.sleep(1)
    
    print("Arming motors")
    vehicle.mode = VehicleMode("ALT_HOLD")
    while not vehicle.mode.name == "ALT_HOLD":
        print(f"Waiting for mode change... Current mode: {vehicle.mode.name}")
        time.sleep(1)
    print("Vehicle mode set to ALT_HOLD.")
    
    vehicle.armed = True
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
    print("Vehicle is armed.")
    
    print("Taking off!")
    thrust = 0.6
    ascent_rate = 0.05  # Adjust this value for ascent speed
    altitude_reached = False
    
    while not altitude_reached:
        current_altitude = vehicle.rangefinder.distance  # Use rangefinder if available
        print(f"Current altitude: {current_altitude} meters")
        
        if current_altitude >= target_altitude * 0.95:
            print(f"Reached target altitude: {current_altitude} meters")
            altitude_reached = True
            break
        else:
            # Increase thrust to ascend
            set_thrust(vehicle, thrust)
            thrust += ascent_rate
            if thrust > 0.8:
                thrust = 0.8  # Limit maximum thrust
            time.sleep(0.1)
    
    # Reset thrust to hover
    set_thrust(vehicle, 0.5)
    print("Hovering at target altitude.")

def set_thrust(vehicle, thrust):
    """
    Function to set the thrust (for ALT_HOLD mode).
    Thrust is a value between 0.0 (min) and 1.0 (max).
    """
    pwm_value = 1000 + (thrust * 1000)  # Map thrust to PWM (1000-2000)
    vehicle.channels.overrides['3'] = int(pwm_value)
    print(f"Setting throttle to {vehicle.channels.overrides['3']}")

def land(vehicle):
    """
    Lands the drone.
    """
    print("Initiating landing sequence...")
    vehicle.mode = VehicleMode("LAND")
    while vehicle.mode.name != "LAND":
        print(f"Waiting for mode change... Current mode: {vehicle.mode.name}")
        time.sleep(1)
    print("Vehicle mode set to LAND.")
    
    # Wait for the vehicle to land
    while vehicle.armed:
        current_altitude = vehicle.rangefinder.distance
        print(f"Current altitude during landing: {current_altitude} meters")
        time.sleep(1)
    print("Vehicle has landed and disarmed.")

def main():
    # List of potential serial devices
    devices = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyUSB2', '/dev/ttyUSB3']

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

    # Arm and take off to 3 feet (~0.9 meters)
    target_altitude = 0.9  # 3 feet in meters
    try:
        arm_and_takeoff_nogps(vehicle, target_altitude)
        print("Hovering...")
        time.sleep(5)  # Hover for 5 seconds

        # Land the vehicle
        land(vehicle)
    finally:
        # Disarm and close the vehicle connection
        if vehicle.armed:
            print("Disarming the vehicle...")
            vehicle.armed = False
            while vehicle.armed:
                print("Waiting for vehicle to disarm...")
                time.sleep(1)
            print("Vehicle is disarmed.")
        vehicle.channels.overrides = {}
        vehicle.close()
        print("Vehicle connection closed.")

if __name__ == "__main__":
    main()
