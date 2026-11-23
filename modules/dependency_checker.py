
from modules.detector import detect_all_tools
from modules.version_checker import check_all_versions


def check_dependencies():

    detected_tools = detect_all_tools()

    version_results = check_all_versions(detected_tools)

    missing = []
    incompatible = []

    for tool in version_results:

        if tool["status"] == "NOT INSTALLED":
            missing.append(tool["name"])

        elif tool["status"] == "UPDATE REQUIRED":
            incompatible.append(tool["name"])

    return {
        "missing": missing,
        "incompatible": incompatible
    }


def display_dependencies():

    result = check_dependencies()

    print("\n========== DEPENDENCY REPORT ==========")

    print("\nMissing Dependencies:")

    if result["missing"]:
        for tool in result["missing"]:
            print("-", tool)
    else:
        print("None")

    print("\nIncompatible Dependencies:")

    if result["incompatible"]:
        for tool in result["incompatible"]:
            print("-", tool)
    else:
        print("None")

    print("=======================================")

    return result
