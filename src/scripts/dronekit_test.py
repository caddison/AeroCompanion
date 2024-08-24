from dronekit import connect

# Global variable to store the vehicle instance
vehicle = None

def connect_vehicle(connection_string: str):
    global vehicle
    print(f"Connecting to vehicle on: {connection_string}")
    vehicle = connect(connection_string, baud=115200, wait_ready=True)

    # Print some vehicle attributes (state)
    print("Autopilot Firmware version: %s" % vehicle.version)
    print("Global Location: %s" % vehicle.location.global_frame)
    print("Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
    print("Local Location: %s" % vehicle.location.local_frame)
    print("Attitude: %s" % vehicle.attitude)
    print("Velocity: %s" % vehicle.velocity)
    print("Battery: %s" % vehicle.battery)
    print("Last Heartbeat: %s" % vehicle.last_heartbeat)
    print("Is Armable?: %s" % vehicle.is_armable)
    print("System status: %s" % vehicle.system_status.state)
    print("Mode: %s" % vehicle.mode.name)

def close_vehicle():
    global vehicle
    if vehicle is not None:
        vehicle.close()
        print("Vehicle connection closed")

if __name__ == '__main__':
    connect_vehicle('/dev/ttyACM0')

    # Keep this script running or do other tasks as needed
    # To close the vehicle, you can call close_vehicle()
