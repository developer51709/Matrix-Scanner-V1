import os
import platform
import subprocess

def is_termux():
    return (
        "com.termux" in os.getenv("PREFIX", "") or
        os.path.exists("/data/data/com.termux/files/usr")
    )

def is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        # Windows has no geteuid()
        return False

def has_su_binary():
    return (
        os.path.exists("/system/bin/su") or
        os.path.exists("/system/xbin/su")
    )

def try_su():
    try:
        out = subprocess.run(["su", "-c", "id"], capture_output=True, text=True)
        return "uid=0" in out.stdout
    except Exception:
        return False

def detect_environment():
    system = platform.system().lower()

    # Base OS
    if system == "windows":
        return {
            "os": "windows",
            "env": "windows",
            "root": False,
            "capabilities": {
                "system_logs": False,
                "system_users": True,
                "network_scan": True,
                "package_audit": False
            }
        }

    if system == "darwin":
        return {
            "os": "macos",
            "env": "macos",
            "root": is_root(),
            "capabilities": {
                "system_logs": True,
                "system_users": True,
                "network_scan": True,
                "package_audit": True
            }
        }

    # Linux or Android/Termux
    if system == "linux":
        if is_termux():
            rooted = is_root() or has_su_binary() or try_su()
            return {
                "os": "android",
                "env": "termux_root" if rooted else "termux",
                "root": rooted,
                "capabilities": {
                    "system_logs": rooted,
                    "system_users": rooted,
                    "network_scan": True,
                    "package_audit": True,
                    "termux_api": os.path.exists("/data/data/com.termux/files/usr/bin/termux-info")
                }
            }

        # Traditional Linux
        rooted = is_root()
        return {
            "os": "linux",
            "env": "linux_root" if rooted else "linux_user",
            "root": rooted,
            "capabilities": {
                "system_logs": True,
                "system_users": True,
                "network_scan": True,
                "package_audit": True
            }
        }

    # Fallback
    return {
        "os": "unknown",
        "env": "unknown",
        "root": False,
        "capabilities": {}
    }