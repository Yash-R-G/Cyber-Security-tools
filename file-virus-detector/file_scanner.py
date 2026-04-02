import os

# Suspicious file extensions (common malware types)
SUSPICIOUS_EXTENSIONS = [".exe", ".bat", ".vbs", ".ps1", ".scr"]

# Suspicious keywords in file names
SUSPICIOUS_NAMES = ["virus", "trojan", "hack", "keylog", "malware"]


def scan_directory(path):
    print(f"\n[+] Scanning folder: {path}\n")

    found = False

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_lower = file.lower()

            # Check extension
            for ext in SUSPICIOUS_EXTENSIONS:
                if file_lower.endswith(ext):
                    print(f"[WARNING] Suspicious file type: {file_path}")
                    found = True

            # Check file name
            for keyword in SUSPICIOUS_NAMES:
                if keyword in file_lower:
                    print(f"[ALERT] Suspicious file name: {file_path}")
                    found = True

    if not found:
        print("[OK] No suspicious files found")


def main():
    print("=== File Virus Detection Tool ===")

    folder = input("Enter folder path to scan: ")

    if os.path.exists(folder):
        scan_directory(folder)
    else:
        print("[ERROR] Invalid folder path")


if __name__ == "__main__":
    main()
