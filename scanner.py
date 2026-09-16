import socket

# target we scanning.
target = "scanme.nmap.org"
port = 80  # Port 80 standard port for(HTTP)

print(f"Testing connection to {target} on port {port}...")

# Create socket 
# AF_INET= IPv4 address. SOCK_STREAM = TCP.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   socket wait - maximum of 2 seconds for a reply
s.settimeout(2)

#  Attempt to connect. 'connect_ex' returns an error code. 
# returns  0, connection was a success
result = s.connect_ex((target, port))

if result == 0:
    print(f"Result: Port {port} is OPEN! 🔓")
else:
    print(f"Result: Port {port} is CLOSED. 🔒")

# 4. end connection
s.close()