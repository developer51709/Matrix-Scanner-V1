# modules/process_scan.py

import subprocess
import platform

name = "Process Scan"
description = "Lists running processes."
supported = ["linux", "linux_root", "android", "termux", "termux_root", "windows", "macos"]

def run(env):
    print(f"[{name}] Scanning running processes...")

    system = platform.system().lower()

    try:
        if system == "windows":
            cmd = ["tasklist"]
        else:
            cmd = ["ps", "aux"]

        result = subprocess.run(cmd, capture_output=True, text=True)
        processes = result.stdout.splitlines()

        print(f"[{name}] Found {len(processes)} processes.\n")
        return processes

    except Exception as e:
        print(f"[{name}] Error: {e}\n")
        return []