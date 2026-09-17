import socket
import concurrent.futures
import argparse
import time

# A dictionary to map port numbers to their actual service names
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

parser = argparse.ArgumentParser(description="NightEyes0 Network Scanner")
parser.add_argument("-t", "--target", help="The target IP address or domain to scan", required=True)
args = parser.parse_args()
target = args.target

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    if result == 0:
        # Get the service name from our dictionary, or default to "Unknown"
        service = COMMON_PORTS.get(port, "Unknown")
        # The :<10 makes sure the columns line up perfectly with 10 spaces
        print(f"{port:<10} [ OPEN ]    {service}")
        
    s.close()

# --- THE NEW PROFESSIONAL UI ---
print("=" * 50)
print("    NIGHTEYES0 NETWORK SCANNER v1.0")
print("=" * 50)
print(f"Target: {target}")
print("Scanning ports 1 to 1000...")
print("-" * 50)
print("PORT       STATUS      SERVICE")
print("-" * 50)

# Start the stopwatch
start_time = time.time()

# We increased the range to 1000 to show off the multi-threading!
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1001))

# Stop the stopwatch
end_time = time.time()
total_time = end_time - start_time

print("-" * 50)
print(f"Scan completed in {total_time:.2f} seconds.")
print("=" * 50)