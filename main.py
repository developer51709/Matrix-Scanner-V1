import os
import time
import importlib
import shutil

# Import OS detection module
from modules.os_detect import detect_environment

# ANSI colors
CYAN = "\033[36m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

ASCII_ART = r"""
╭──────────────────────────╮
│ ╭─╮   ╭─╮╭──────╮╭─────╮ │
│ │ ╰╮ ╭╯ ││ ╭──╮ │╰─╮ ╭─╯ │
│ │  ╰─╯  ││ ╰──╯ │  │ │   │
│ │ ╭╮ ╭╮ ││ ╭──╮ │  │ │   │
│ │ │╰─╯│ ││ │  │ │  │ │   │
│ ╰─╯   ╰─╯╰─╯  ╰─╯  ╰─╯   │
│ ╭──────╮ ╭─────╮ ╭─╮ ╭─╮ │
│ │ ╭──╮ │ ╰─╮ ╭─╯ │ │ │ │ │
│ │ ╰──╯╭╯   │ │   ╰╮╰─╯╭╯ │
│ │ ╭──╮╰╮   │ │   ╭╯╭─╮╰╮ │
│ │ │  │ │ ╭─╯ ╰─╮ │ │ │ │ │
│ ╰─╯  ╰─╯ ╰─────╯ ╰─╯ ╰─╯ │
╰──────────────────────────╯
╭──────────────────────────╮
│     MATRIX SCANNER V1    │
╰──────────────────────────╯
"""

DISCLAIMER_TEXT = r"""
╭──────────────────────────╮
│ This tool is intended    │
│ for authorized security  │
│ testing, research, and   │
│ educational use.         │
│ Unauthorized access to   │
│ systems you do not own   │
│ or have explicit         │
│ permission to test is    │
│ illegal.                 │
│                          │
│ By continuing, you       │
│ acknowledge full         │
│ responsibility for your  │
│ actions.                 │
╰──────────────────────────╯
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def center_block(text):
    width = shutil.get_terminal_size().columns
    return "\n".join(line.center(width) for line in text.splitlines())

def boot_sequence():
    clear()
    print(GREEN + center_block(ASCII_ART) + RESET)
    time.sleep(3)

    clear()
    print(RED + center_block(DISCLAIMER_TEXT) + RESET)
    time.sleep(4)

    clear()

def load_module(module_name):
    try:
        module = importlib.import_module(f"modules.{module_name}")
        return module
    except ImportError:
        print(f"{RED}Module '{module_name}' not found.{RESET}")
        return None

def main_menu(env):
    while True:
        print(center_block(f"{GREEN}╭──────────────────────────╮{RESET}"))
        print(center_block(f"{GREEN}   │{RESET}    MATRIX SCANNER MENU   {GREEN}│{RESET}"))
        print(center_block(f"{GREEN}╰──────────────────────────╯{RESET}"))
        print()
        print("1) Run Full Scan")
        print("2) Run Specific Module")
        print("3) Show Environment Info")
        print("4) Exit")
        print()

        choice = input("Select an option: ").strip()

        if choice == "1":
            run_full_scan(env)

        elif choice == "2":
            run_specific_module(env)

        elif choice == "3":
            print("\nDetected Environment:")
            print(env)
            print()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice.\n")

def run_full_scan(env):
    print("\nRunning full scan...\n")

    # Automatically load all modules except os_detect
    module_dir = "modules"
    for file in os.listdir(module_dir):
        if file.endswith(".py") and file not in ["__init__.py", "os_detect.py"]:
            module_name = file[:-3]
            module = load_module(module_name)
            if module:
                if hasattr(module, "run"):
                    print(f"Running module: {module_name}")
                    module.run(env)
                else:
                    print(f"Module '{module_name}' has no run() function.")

    print("\nFull scan complete.\n")

def run_specific_module(env):
    module_name = input("Enter module name: ").strip()
    module = load_module(module_name)

    if module and hasattr(module, "run"):
        module.run(env)
    else:
        print("Invalid module or missing run() function.\n")

def main():
    boot_sequence()
    env = detect_environment()
    main_menu(env)

if __name__ == "__main__":
    main()