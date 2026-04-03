import psutil

# Words that might indicate suspicious programs
SUSPICIOUS_KEYWORDS = ["keylog", "logger", "spy", "capture"]

def check_processes():
    print("\n[+] Scanning running processes...\n")

    found = False

    for process in psutil.process_iter(['pid', 'name']):
        try:
            name = process.info['name'].lower()

            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in name:
                    print(f"[ALERT] Suspicious process found: {name} (PID: {process.info['pid']})")
                    found = True

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found:
        print("[OK] No suspicious processes found")


def check_network_connections():
    print("\n[+] Checking network connections...\n")

    connections = psutil.net_connections()

    for conn in connections:
        if conn.raddr:
            print(f"[INFO] Active connection → IP: {conn.raddr.ip}, Port: {conn.raddr.port}")


def main():
    print("=== Keylogger Activity Detector ===")

    check_processes()
    check_network_connections()

    print("\n[✓] Scan completed")


if __name__ == "__main__":
    main()
