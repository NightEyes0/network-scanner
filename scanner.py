import socket

target = "scanme.nmap.org"

print(f"Scanning target: {target}")
print("Scanning ports 1 to 100 (this might take a minute)...\n")

# A loop that goes from 1 to 100
for port in range(1, 101):
    
    #  NEW socket for this specific port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # timeout to 0.5 seconds 
    s.settimeout(0.5)
    
    #  Attempt  connection
    result = s.connect_ex((target, port))
    
    # 4.  prints  if the port is OPEN 
    if result == 0:
        print(f"[+] Port {port} is OPEN 🔓")
        
    # 5. Close socket 
    s.close()

print("\nScan complete!")