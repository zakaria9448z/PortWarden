import socket
import sys
import time
from datetime import timedelta
import json
import argparse
import os
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
COMMON_PORTS = {
    7: "Echo",
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "RPC",
    137: "NetBIOS Name",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    500: "ISAKMP",
    514: "Syslog",
    520: "RIP",
    587: "SMTP (TLS)",
    631: "IPP Printer",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1194: "OpenVPN",
    1433: "MSSQL",
    1521: "Oracle DB",
    1701: "L2TP",
    1723: "PPTP",
    1812: "RADIUS",
    1813: "RADIUS Accounting",
    2049: "NFS",
    2082: "cPanel",
    2083: "cPanel SSL",
    2086: "WHM",
    2087: "WHM SSL",
    2181: "ZooKeeper",
    2222: "Direct Admin Panel",
    2375: "Docker API",
    2376: "Docker API TLS",
    27017: "MongoDB",
    27018: "MongoDB",
    28017: "MongoDB HTTP",
    3000: "Custom App / Dev",
    3306: "MySQL",
    3389: "RDP",
    4000: "Custom App / Dev",
    4444: "Metasploit / Custom",
    5000: "Custom App / Dev",
    5432: "PostgreSQL",
    5500: "VNC",
    5900: "VNC",
    5984: "CouchDB",
    6379: "Redis",
    7001: "WebLogic",
    7077: "Resin / Java",
    7474: "Neo4j",
    8000: "Custom App / Dev",
    8009: "AJP",
    8080: "HTTP Alt",
    8081: "HTTP Alt 2",
    8443: "plesk",
    8888: "HTTP Alt 3",
    9000: "FastCGI",
    9042: "Cassandra",
    9060: "JBoss",
    9090: "Portainer / Custom",
    9200: "Elasticsearch",
    9300: "Elasticsearch Cluster",
    10000: "Webmin",
    11211: "Memcached",
    15672: "RabbitMQ",
    27017: "MongoDB",
    50030: "Hadoop",
    50070: "Hadoop NameNode",
}

total_ports = 65535
scanned = 0
lock = threading.Lock()
start_time = time.time()
OS = platform.system()

open_ports_list = []


def update_progress():
    global scanned
    with lock:
        scanned += 1
        percent = (scanned / total_ports) * 100
        elapsed = time.time() - start_time
        eta = (elapsed / scanned) * (total_ports - scanned) if scanned > 0 else 0

        msg = f"Scanning: {percent:.1f}% | Scanned: {scanned}/{total_ports} | ETA: {str(timedelta(seconds=int(eta)))}"

        if OS == "Windows":
            print(" " * 100, end="\r")
            print(msg, end="")
        else:
            print(f"\r{msg}", end="")


def scan_port(port, target_ip, filename):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)
            if sock.connect_ex((target_ip, port)) == 0:
                service = COMMON_PORTS.get(port, "Unknown Service")
                entry = {"port": port, "service": service}
                with lock:
                    open_ports_list.append(entry)
                    with open(filename, 'a') as f:
                        json.dump(entry, f)
                        f.write(',\n')
                return entry
    except Exception:
        pass
    return None


def scan_ports(target):
    global scanned
    scanned = 0

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[-] Hostname could not be resolved.")
        return

    print(f"\n[+] Scanning target: {target_ip}")
    print("{:<6} {:<15} {:<20}".format("Port", "Status", "Service"))

    filename = f"{target_ip}.json"


    with open(filename, 'w') as f:
        f.write("[\n")

    results = []

    with ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(scan_port, port, target_ip, filename) for port in range(1, 65536)]

        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)
                print(f"{result['port']:<6} {'Open':<15} {result['service']}")
            update_progress()


    with open(filename, 'rb+') as f:
        f.seek(-2, os.SEEK_END)
        f.truncate()
    with open(filename, 'a') as f:
        f.write("\n]")

    print("\n\n[+] Scan Complete.")
    print(f"[+] Found {len(open_ports_list)} open ports.")
    print(f"[+] Results saved to: {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced TCP Port Scanner - Final Version")
    parser.add_argument("host", help="Target host (IP or domain)")
    args = parser.parse_args()

    scan_ports(args.host)
