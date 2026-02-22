# modules/network_scan.py

import subprocess
import platform

name = "Network Port Scan"
description = "Lists open/listening ports on the local device."
supported = ["linux", "linux_root", "android", "termux", "termux_root", "windows", "macos"]

def run(env):
    print(f"[{name}] Checking open ports...")

    system = platform.system().lower()

    try:
        if system == "windows":
            cmd = ["netstat", "-ano"]
        else:
            # Termux, Linux, macOS
            cmd = ["ss", "-tuln"]

        result = subprocess.run(cmd, capture_output=True, text=True)
        ports = result.stdout.splitlines()

        print(f"[{name}] Found {len(ports)} entries.\n")
        return ports

    except Exception as e:
        print(f"[{name}] Error: {e}\n")
        return []