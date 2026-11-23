
import subprocess
import shutil
import platform

INSTALL_COMMANDS = {
    "KiCad": {
        "manager": "winget",
        "package": "KiCad.KiCad"
    }
}


def check_package_manager():
    if platform.system() == "Windows":
        return shutil.which("winget")
    return None


def install_tool(tool_name):
    if tool_name == "Ngspice":
        print("Automatic installation is not configured for Ngspice.")
        print("Please install Ngspice manually.")
        return False

    if tool_name not in INSTALL_COMMANDS:
        print("Installation is not supported for this tool.")
        return False

    manager = check_package_manager()

    if not manager:
        print("Winget is not available on this system.")
        return False

    package = INSTALL_COMMANDS[tool_name]["package"]

    print(f"\nInstalling {tool_name}...")

    command = [
        manager,
        "install",
        "--id", package,
        "--exact",
        "--accept-package-agreements",
        "--accept-source-agreements"
    ]

    try:
        result = subprocess.run(command)

        if result.returncode == 0:
            print(f"{tool_name} installation completed.")
            return True

        print("Installation failed. Exit code:", result.returncode)
        return False

    except (OSError, subprocess.SubprocessError) as error:
        print("Installation error:", error)
        return False
