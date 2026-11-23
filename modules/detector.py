
import shutil
import subprocess
import platform
import os

TOOLS = {
    "Ngspice": {
        "commands": ["ngspice"],
        "version_args": ["--version"]
    },
    "KiCad": {
        "commands": ["kicad-cli"],
        "version_args": ["version"],
        "windows_paths": [
            os.path.expandvars(
                r"%LOCALAPPDATA%\Programs\KiCad\10.0\bin\kicad-cli.exe"
            )
        ]
    },
    "Python": {
        "commands": ["python", "python3"],
        "version_args": ["--version"]
    },
    "Git": {
        "commands": ["git"],
        "version_args": ["--version"]
    }
}


def get_system_info():
    return platform.system()


def detect_tool(tool_name, tool_info):
    executable = None

    for command in tool_info["commands"]:
        executable = shutil.which(command)
        if executable:
            break

    if not executable and platform.system() == "Windows":
        for path in tool_info.get("windows_paths", []):
            if os.path.isfile(path):
                executable = path
                break

    if executable:
        try:
            result = subprocess.run(
                [executable] + tool_info["version_args"],
                capture_output=True,
                text=True,
                timeout=15
            )

            version = result.stdout.strip() or result.stderr.strip()

            return {
                "name": tool_name,
                "installed": True,
                "version": version,
                "path": executable
            }

        except (subprocess.SubprocessError, OSError) as error:
            return {
                "name": tool_name,
                "installed": True,
                "version": "Could not retrieve version",
                "path": executable,
                "error": str(error)
            }

    return {
        "name": tool_name,
        "installed": False,
        "version": None,
        "path": None
    }


def detect_all_tools():
    results = []

    for tool_name, tool_info in TOOLS.items():
        results.append(detect_tool(tool_name, tool_info))

    return results
