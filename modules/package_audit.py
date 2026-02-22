# modules/package_audit.py

import subprocess
import platform

name = "Package Audit"
description = "Lists installed packages (Termux, Linux, macOS, Windows)."
supported = ["linux", "linux_root", "android", "termux", "termux_root", "windows", "macos"]

def run(env):
    print(f"[{name}] Checking installed packages...")

    system = platform.system().lower()

    try:
        if env["env"] in ["termux", "termux_root"]:
            cmd = ["pkg", "list-installed"]
        elif system == "linux":
            cmd = ["dpkg", "-l"]
        elif system == "darwin":
            cmd = ["brew", "list"]
        elif system == "windows":
            cmd = ["wmic", "product", "get", "name"]
        else:
            print(f"[{name}] Unsupported environment.\n")
            return []

        result = subprocess.run(cmd, capture_output=True, text=True)
        packages = result.stdout.splitlines()

        print(f"[{name}] Found {len(packages)} packages.\n")
        return packages

    except Exception as e:
        print(f"[{name}] Error: {e}\n")
        return []