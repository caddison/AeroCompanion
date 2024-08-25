from dronekit import connect, VehicleMode
import time

# Connect to the drone
print("Connecting to drone...", flush=True)
vehicle = connect('/dev/ttyACM0', baud=115200, wait_ready=True)

# Function to arm the drone
def arm_drone():
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable...", flush=True)
        time.sleep(1)

    print("Arming the drone...", flush=True)
    vehicle.mode = VehicleMode("STABILIZE")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for drone to arm...", flush=True)
        time.sleep(1)

    print("Drone is armed!", flush=True)

# Function to monitor and output the drone's status to the console
def monitor_drone():
    try:
        while True:
            print("----------", flush=True)
            print(f"Mode: {vehicle.mode.name}", flush=True)
            print(f"Altitude: {vehicle.location.global_relative_frame.alt:.2f} m", flush=True)
            print(f"Latitude: {vehicle.location.global_frame.lat:.6f}", flush=True)
            print(f"Longitude: {vehicle.location.global_frame.lon:.6f}", flush=True)
            print(f"Ground Speed: {vehicle.groundspeed:.2f} m/s", flush=True)
            print(f"Air Speed: {vehicle.airspeed:.2f} m/s", flush=True)

            battery_voltage = f"{vehicle.battery.voltage:.2f} V" if vehicle.battery.voltage else "N/A"
            battery_level = f"({vehicle.battery.level}%)" if vehicle.battery.level else "(N/A)"
            print(f"Battery: {battery_voltage} {battery_level}", flush=True)

            if vehicle.battery.current is not None:
                print(f"Battery Current: {vehicle.battery.current:.2f} A", flush=True)
            else:
                print("Battery Current: N/A", flush=True)

            print(f"GPS Fix Type: {vehicle.gps_0.fix_type}", flush=True)
            print(f"Satellites Visible: {vehicle.gps_0.satellites_visible}", flush=True)
            print(f"Armed: {vehicle.armed}", flush=True)
            print(f"EKF Status: {vehicle.ekf_ok}", flush=True)
            print(f"Attitude: Roll={vehicle.attitude.roll:.2f}, "
                  f"Pitch={vehicle.attitude.pitch:.2f}, "
                  f"Yaw={vehicle.attitude.yaw:.2f}", flush=True)
            print(f"Heading: {vehicle.heading} degrees", flush=True)
            print(f"Last Heartbeat: {vehicle.last_heartbeat:.2f} seconds ago", flush=True)
            print("----------", flush=True)

            # Add a delay to prevent spamming the console
            time.sleep(30)
    except KeyboardInterrupt:
        print("Exiting...", flush=True)
    finally:
        print("Closing connection...", flush=True)
        vehicle.close()

# Run the arm and monitor functions
arm_drone()
monitor_drone()
