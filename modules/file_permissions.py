# modules/file_permissions.py

import os

name = "File Permission Audit"
description = "Checks for world-writable files in home directory."
supported = ["linux", "linux_root", "android", "termux", "termux_root", "windows", "macos"]

def run(env):
    print(f"[{name}] Scanning for insecure file permissions...")

    home = os.path.expanduser("~")
    findings = []

    for root, dirs, files in os.walk(home):
        for f in files:
            path = os.path.join(root, f)
            try:
                mode = os.stat(path).st_mode
                if mode & 0o002:
                    findings.append(path)
            except:
                pass

    print(f"[{name}] Found {len(findings)} world-writable files.\n")
    return findings