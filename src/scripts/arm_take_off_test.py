from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the Pixhawk
vehicle = connect('/dev/ttyACM0', wait_ready=True, baud=115200)

def arm_and_takeoff_nogps(target_altitude):
    """
    Arms the drone and takes off to a specified altitude using non-GPS modes.
    """
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable...")
        time.sleep(1)
    
    print("Arming motors")
    vehicle.mode = VehicleMode("STABILIZE")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
    
    print("Taking off in Stabilize mode")
    thrust = 0.6
    vehicle.mode = VehicleMode("ALT_HOLD")
    
    while True:
        current_altitude = vehicle.rangefinder.distance
        if current_altitude >= target_altitude * 0.95:
            print(f"Reached target altitude: {current_altitude} meters")
            break
        elif current_altitude < target_altitude * 0.6:
            thrust = 0.65  # Increase thrust to climb faster
        elif current_altitude > target_altitude * 0.9:
            thrust = 0.5  # Reduce thrust as we approach the target altitude
        
        set_thrust(thrust)
        time.sleep(0.1)

def set_thrust(thrust):
    """
    Function to set the thrust (for ALT_HOLD mode).
    Thrust is a value between 0.0 (min) and 1.0 (max).
    """
    vehicle.channels.overrides['3'] = 1500 + int(thrust * 500)

def land():
    """
    Lands the drone.
    """
    print("Landing...")
    vehicle.mode = VehicleMode("LAND")
    while vehicle.armed:
        print("Waiting for landing...")
        time.sleep(1)
    print("Landed successfully")

# Main execution
try:
    arm_and_takeoff_nogps(3)  # Take off to 3 meters
    print("Hovering...")
    time.sleep(10)  # Hover for 10 seconds
    land()

finally:
    print("Closing vehicle connection")
    vehicle.close()
