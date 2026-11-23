
import re


MINIMUM_VERSIONS = {
    "Ngspice": "40",
    "KiCad": "8.0",
    "Python": "3.10",
    "Git": "2.30"
}


def extract_version(version_text):

    if not version_text:
        return None

    match = re.search(r"\d+(?:\.\d+)+", version_text)

    if match:
        return match.group()

    return None


def compare_versions(installed, required):

    installed_parts = tuple(map(int, installed.split(".")))
    required_parts = tuple(map(int, required.split(".")))

    length = max(len(installed_parts), len(required_parts))

    installed_parts += (0,) * (length - len(installed_parts))
    required_parts += (0,) * (length - len(required_parts))

    return installed_parts >= required_parts


def check_version(tool):

    name = tool["name"]

    if not tool["installed"]:
        return {
            "name": name,
            "status": "NOT INSTALLED",
            "installed_version": None,
            "required_version": MINIMUM_VERSIONS[name]
        }

    installed_version = extract_version(tool["version"])

    if installed_version is None:
        status = "VERSION UNKNOWN"

    elif compare_versions(
        installed_version,
        MINIMUM_VERSIONS[name]
    ):
        status = "COMPATIBLE"

    else:
        status = "UPDATE REQUIRED"

    return {
        "name": name,
        "status": status,
        "installed_version": installed_version,
        "required_version": MINIMUM_VERSIONS[name]
    }


def check_all_versions(tools):

    results = []

    for tool in tools:
        results.append(check_version(tool))

    return results
