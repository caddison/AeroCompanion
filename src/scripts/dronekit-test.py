from dronekit import connect, VehicleMode

# Connect to the Vehicle
print("Connecting to vehicle on: /dev/ttyACM0")
vehicle = connect('/dev/ttyACM0', baud=115200, wait_ready=True)

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

# Close vehicle object before exiting script
vehicle.close()
