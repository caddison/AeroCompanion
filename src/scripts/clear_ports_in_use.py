import os
import subprocess
import sys
import time

def find_process_using_port(port):
    """Find the process ID (PID) that is using the given port."""
    command = f"lsof -i :{port} | grep LISTEN"
    try:
        output = subprocess.check_output(command, shell=True).decode().strip()
        if output:
            # Extract the PID from the output
            pid = int(output.split()[1])
            return pid
        else:
            return None
    except subprocess.CalledProcessError:
        return None

def kill_process(pid):
    """Kill the process with the given PID."""
    try:
        os.kill(pid, 9)
        print(f"Process with PID {pid} has been terminated.")
    except OSError as e:
        print(f"Failed to terminate process with PID {pid}: {e}")

def free_ports_and_restart(port_list, restart_command):
    """Free the ports and restart the application."""
    for port in port_list:
        pid = find_process_using_port(port)
        if pid:
            print(f"Port {port} is in use by process with PID {pid}.")
            kill_process(pid)
        else:
            print(f"Port {port} is not in use.")
    
    # Optionally wait a bit before restarting
    time.sleep(2)
    
    # Restart the application
    subprocess.Popen(restart_command, shell=True)
    print(f"Restarted application with command: {restart_command}")

if __name__ == "__main__":
    # Define the ports to check
    ports_to_check = [8080, 3000]
    
    # Define the command to restart your application (adjust as needed)
    restart_cmd = "npm run start-all" 

    # Free the ports and restart the application
    free_ports_and_restart(ports_to_check, restart_cmd)
