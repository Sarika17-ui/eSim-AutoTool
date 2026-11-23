
from modules.detector import detect_all_tools, get_system_info
from modules.version_checker import check_all_versions
from modules.dependency_checker import display_dependencies
from modules.installer import install_tool


def main():

    print("================================")
    print("       eSim AutoTool")
    print("================================")

    print("Operating System:", get_system_info())

    detected_tools = detect_all_tools()

    print("\n========== TOOL STATUS ==========")

    for tool in check_all_versions(detected_tools):

        print("\nTool:", tool["name"])
        print("Status:", tool["status"])
        print("Installed Version:", tool["installed_version"])
        print("Minimum Required:", tool["required_version"])

    dependency_report = display_dependencies()

    if dependency_report["missing"]:

        print("\nMissing tools can be installed.")

        choice = input("Do you want to install a missing tool? (yes/no): ")

        if choice.lower() == "yes":

            print("\nAvailable tools:", ", ".join(dependency_report["missing"]))

            tool_name = input("Enter tool name: ").strip()

            if tool_name in dependency_report["missing"]:
                install_tool(tool_name)
            else:
                print("Invalid tool selection.")

    print("\nAutoTool execution completed.")


if __name__ == "__main__":
    main()
