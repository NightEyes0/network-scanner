# Multi-threaded Network Scanner 

A fast, command-line TCP port scanner built in Python with live OSINT geolocation, demonstrating socket programming and concurrent execution.

# Overview
This cybersecurity tool allows users to scan remote servers or local networks to identify open ports and active services. By utilizing Python's `ThreadPoolExecutor`, the scanner achieves massive performance gains. It also integrates with the IP-API to perform real-time target geolocation (OSINT)

# Technical Skills Demonstrated
* Networking: TCP/IPv4 protocols, port resolution, and socket connection handling.
* Multi-threading: Asynchronous execution using `concurrent.futures`.
* API Integration: Live JSON parsing from third-party OSINT databases.
* CLI Development: Robust terminal input handling using `argparse`.

# Example Output
```text
==================================================
    NIGHTEYES0 NETWORK SCANNER v1.1
==================================================
Target:   scanme.nmap.org
Location: Fremont, United States (ISP: Linode)
Scanning ports 1 to 1000...
--------------------------------------------------
PORT       STATUS      SERVICE
22         [ OPEN ]    SSH
80         [ OPEN ]    HTTP
--------------------------------------------------
Scan completed in 1.24 seconds.
==================================================

# To Run
pip install requests
python scanner.py --target scanme.nmap.org
