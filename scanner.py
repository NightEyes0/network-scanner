import socket
import concurrent.futures

target = "scanme.nmap.org"

#  socket logic inside a function
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN 🔓")
        
    s.close()

print(f"Scanning target: {target}")
print("Scanning ports 1 to 100 using multi-threading...\n")


# 100  (threads) to run at the exact same time.
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # 'map' runs the 'scan_port' function on numbers 1 through 100
    executor.map(scan_port, range(1, 101))

print("\nScan complete!")