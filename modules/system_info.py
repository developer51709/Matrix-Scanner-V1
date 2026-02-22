# modules/system_info.py

import platform
import os
import shutil

name = "System Information"
description = "Collects detailed system, environment, and capability information."
supported = ["linux", "linux_root", "android", "termux", "termux_root", "windows", "macos"]

def run(env):
    print(f"[{name}] Collecting detailed system information...\n")

    info = {
        "OS": env["os"],
        "Environment": env["env"],
        "Root Access": env["root"],
        "Platform String": platform.platform(),
        "Python Version": platform.python_version(),
        "Machine Type": platform.machine(),
        "Processor": platform.processor(),
        "CPU Count": os.cpu_count(),
        "Terminal Size": shutil.get_terminal_size().columns,
        "Capabilities": env["capabilities"]
    }

    for key, value in info.items():
        print(f"  {key}: {value}")

    print(f"\n[{name}] Completed.\n")
    return info