# modules/system_info.py

import platform
import os

name = "System Information"
description = "Collects basic system and environment information."
supported = ["linux", "linux_root", "android", "termux", "termux_root", "windows", "macos"]

def run(env):
    print(f"[{name}] Collecting system information...")

    info = {
        "os": env["os"],
        "environment": env["env"],
        "root": env["root"],
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }

    for k, v in info.items():
        print(f"  {k}: {v}")

    print(f"[{name}] Done.\n")
    return info