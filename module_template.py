# modules/module_template.py

name = "Template Module"
description = "Describe what this module checks."
supported = ["linux", "linux_root", "android", "termux", "termux_root", "windows", "macos"]

def run(env):
    print(f"[{name}] Starting scan...")

    # Do your checks here
    findings = []

    # Example:
    # findings.append({"severity": "low", "message": "Example finding"})

    print(f"[{name}] Completed. Findings: {len(findings)}")
    return findings