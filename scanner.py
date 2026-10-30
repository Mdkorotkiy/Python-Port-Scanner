import pyfiglet
import sys
import socket
from datetime import datetime


def identify_service(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def scan_ports(target):
    print(pyfiglet.figlet_format("PORT SCANNER"))
    print("-" * 55)
    print(f"Scanning Target: {target}")

    start_time = datetime.now()
    print(f"Scan started at: {start_time}")
    print("-" * 55)

    print(f"{'PORT':<12}{'STATE':<12}{'SERVICE'}")
    print("-" * 55)

    open_ports = []

    try:
        for port in range(1, 1025):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))

                if result == 0:
                    service = identify_service(port)
                    open_ports.append(port)

                    print(f"{port:<12}{'OPEN':<12}{service}")

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        return

    except socket.error as error:
        print(f"\nSocket error: {error}")
        return

    print("-" * 55)
    print(f"Total open ports: {len(open_ports)}")
    print(f"Scan duration: {datetime.now() - start_time}")
    print("-" * 55)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            target = socket.gethostbyname(sys.argv[1])
        except socket.gaierror:
            print("Error: Could not resolve hostname.")
            sys.exit(1)
    else:
        target = "127.0.0.1"

    scan_ports(target)
