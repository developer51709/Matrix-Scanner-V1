# modules/process_scan.py

import subprocess
import platform

name = "Process Scan"
description = "Lists running processes with basic analysis."
supported = ["linux", "linux_root", "android", "termux", "termux_root", "windows", "macos"]

SUSPICIOUS_KEYWORDS = ["crypto", "miner", "xmrig", "bot", "rat", "keylog"]

def run(env):
    print(f"[{name}] Scanning running processes...\n")

    system = platform.system().lower()

    try:
        if system == "windows":
            cmd = ["tasklist"]
        else:
            cmd = ["ps", "aux"]

        result = subprocess.run(cmd, capture_output=True, text=True)
        lines = result.stdout.splitlines()

        print(f"  Total processes detected: {len(lines)}")

        suspicious = []
        for line in lines:
            lower = line.lower()
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in lower:
                    suspicious.append(line)

        if suspicious:
            print("\n  Suspicious processes detected:")
            for proc in suspicious:
                print("   →", proc)
        else:
            print("\n  No suspicious processes found.")

        print(f"\n[{name}] Completed.\n")
        return lines

    except Exception as e:
        print(f"[{name}] Error: {e}\n")
        return []