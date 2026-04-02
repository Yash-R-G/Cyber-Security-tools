from keylogger_detector.keylogger_detector import main as keylogger_scan
from file_virus_detector.file_scanner import scan_directory

print("=== Cyber Security Toolkit ===")
print("1. Keylogger Detector")
print("2. File Virus Scanner")

choice = input("Choose option: ")

if choice == "1":
    keylogger_scan()
elif choice == "2":
    path = input("Enter folder path: ")
    scan_directory(path)
else:
    print("Invalid choice")
