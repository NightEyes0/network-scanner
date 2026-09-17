import socket
import concurrent.futures
import argparse
import time
import requests  

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 443: "HTTPS", 3306: "MySQL", 3389: "RDP"
}

parser = argparse.ArgumentParser(description="NightEyes0 Network Scanner")
parser.add_argument("-t", "--target", help="The target IP address or domain to scan", required=True)
args = parser.parse_args()
target = args.target

# Live IP  API
def get_location(target_url):
    try:
        # Ask global database where this server is 
        response = requests.get(f"http://ip-api.com/json/{target_url}")
        data = response.json()
        
        if data['status'] == 'success':
            return f"{data['city']}, {data['country']} (ISP: {data['isp']})"
        else:
            return "Unknown Location"
    except:
        return "Database unreachable"


def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    if result == 0:
        service = COMMON_PORTS.get(port, "Unknown")
        print(f"{port:<10} [ OPEN ]    {service}")
        
    s.close()

print("=" * 50)
print("    NIGHTEYES0 NETWORK SCANNER v1.0")
print("=" * 50)

#call new API function here before the scan 
print(f"Target:   {target}")
print(f"Location: {get_location(target)}")  # Prints live location

print("Scanning ports 1 to 1000...")
print("-" * 50)
print("PORT       STATUS      SERVICE")
print("-" * 50)

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1001))

end_time = time.time()
total_time = end_time - start_time

print("-" * 50)
print(f"Scan completed in {total_time:.2f} seconds.")
print("=" * 50)