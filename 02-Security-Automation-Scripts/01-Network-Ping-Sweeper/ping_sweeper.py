import os
import platform

def run_scanner():
    # Define the network base (local example)
    base_ip = "192.168.1." 

    print(f"--- Starting scan on network {base_ip}0 ---")

    # Scanning the first 10 IPs of the network
    for i in range(1, 11):
        ip = base_ip + str(i)
        
        # Determine the correct flag based on the Operating System
        # Windows uses '-n', while Unix (Linux/macOS) uses '-c'
        param = "-n" if platform.system().lower() == "windows" else "-c"
        
        # Execute the ping command
        # Redirecting output to dev/null or nul to keep the console clean
        null_device = "NUL" if platform.system().lower() == "windows" else "/dev/null"
        response = os.system(f"ping {param} 1 {ip} > {null_device} 2>&1")
        
        if response == 0:
            print(f"[+] Device found: {ip}")
        else:
            print(f"[-] No response from: {ip}")

    print("--- Scan finished ---")

if __name__ == "__main__":
    run_scanner()
