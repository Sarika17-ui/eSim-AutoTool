
# eSim AutoTool

## Overview
eSim AutoTool is a Python-based command-line utility that helps users identify required software tools, check installed versions, detect missing dependencies, and install supported tools.

## Features
- Detects installed tools and their executable paths.
- Checks installed versions against configurable minimum versions.
- Identifies missing and incompatible dependencies.
- Supports KiCad installation through Windows Package Manager (Winget).
- Provides an interactive command-line interface.
- Reports tools that require manual installation.

## Supported Tools

| Tool | Detection | Version Check | Automatic Installation |
|---|---|---|---|
| Ngspice | Yes | Yes | Not configured |
| KiCad | Yes | Yes | Windows Winget |
| Python | Yes | Yes | Not configured |
| Git | Yes | Yes | Not configured |

## Requirements
- Python 3.10 or later
- Windows for the current Winget installation feature
- Winget for automatic KiCad installation

## Project Structure

```text
eSim-AutoTool/
├── main.py
├── requirements.txt
├── README.md
├── DESIGN.md
├── modules/
│   ├── __init__.py
│   ├── detector.py
│   ├── version_checker.py
│   ├── dependency_checker.py
│   └── installer.py
├── tests/
└── logs/
```

## How to Run

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

4. Review the tool and dependency reports.
5. Follow the prompts to install a supported missing tool.

## Installation Support
KiCad is installed using Winget with package ID `KiCad.KiCad`.

Ngspice automatic installation is not currently configured. Users must install it manually.

## Version Configuration
Minimum version thresholds are currently configured in `modules/version_checker.py`. They are prototype defaults and should be adjusted according to the actual eSim environment requirements.

## Limitations
- Automatic installation currently supports KiCad on Windows only.
- Ngspice installation is manual.
- Cross-platform installation support is not yet implemented.

## Future Improvements
- Linux and macOS package manager support.
- Graphical user interface.
- Automatic update management.
- Configuration file for tool versions.
- Automated testing and logging.

## Author
Developed as an eSim Automated Tool Manager internship task prototype.
