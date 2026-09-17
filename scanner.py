import socket
import concurrent.futures
import argparse

#Command-Line Argument
parser = argparse.ArgumentParser(description="NightEyes0 Network Scanner")
parser.add_argument("-t", "--target", help="The target IP address or domain to scan", required=True)
args = parser.parse_args()

# Grab target from the terminal
target = args.target

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN 🔓")
        
    s.close()

print(f"Scanning target: {target}")
print("Scanning ports 1 to 100 using multi-threading...\n")

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 101))

print("\nScan complete!")