
# eSim AutoTool – Design Document

## 1. Introduction
eSim AutoTool is a Python-based command-line application designed to simplify the management of software dependencies required for eSim.

It detects installed tools, checks their versions, identifies missing dependencies, and provides installation support for selected tools.

## 2. Objectives
- Automate software tool detection.
- Verify installed software versions.
- Identify missing and incompatible dependencies.
- Simplify installation of supported tools.
- Provide clear reports through a command-line interface.

## 3. System Architecture

The application follows a modular architecture.

```text
             +----------------------+
             |       main.py        |
             |   Command Line UI    |
             +----------+-----------+
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
   +------------+ +------------+ +------------+
   |  Detector  | |  Version   | | Dependency |
   |   Module   | |  Checker   | |   Checker  |
   +------------+ +------------+ +------------+
          |             |             |
          v             v             v
   +--------------------------------------+
   |       System Tool Information        |
   +--------------------------------------+
                        |
                        v
               +----------------+
               |    Installer   |
               |     Module     |
               +----------------+
                        |
                        v
               +----------------+
               |  Winget / OS   |
               +----------------+

```

## 4. Module Description

### Detector Module
Uses Python libraries such as `shutil`, `subprocess`, and `platform` to identify installed tools and retrieve executable paths and version information.

### Version Checker Module
Extracts version numbers and compares them against configurable minimum version thresholds.

### Dependency Checker Module
Generates a report containing missing and incompatible dependencies.

### Installer Module
Uses Windows Package Manager (Winget) to install supported software. KiCad installation is currently supported. Ngspice requires manual installation.

### Main Module
Provides the command-line interface and coordinates the other modules.

## 5. Technology Stack
- Programming Language: Python 3
- Libraries: subprocess, shutil, platform, re, os
- Package Manager: Windows Package Manager (Winget)
- Development Environment: Visual Studio Code

## 6. Workflow
1. Start the application.
2. Detect the operating system.
3. Search for configured software tools.
4. Retrieve installed versions.
5. Compare versions against minimum thresholds.
6. Generate the dependency report.
7. Ask the user whether to install a missing supported tool.
8. Execute the installation command after user confirmation.
9. Display the execution result.

## 7. Error Handling
- Handles missing executables.
- Handles command execution errors.
- Uses timeouts when retrieving version information.
- Reports unsuccessful installations.
- Avoids attempting automatic installation for unsupported tools.

## 8. Current Limitations
- Automatic installation currently supports KiCad on Windows.
- Ngspice requires manual installation.
- Minimum version thresholds are configurable prototype defaults, not official eSim compatibility guarantees.
- Linux and macOS installation support is not yet implemented.

## 9. Future Enhancements
- Linux and macOS package manager support.
- Graphical user interface.
- Automatic update management.
- Configuration through external files.
- Expanded automated test coverage.
