# Battery Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, cross-platform battery monitor application built with Python and PySide6 (Qt for Python). This application displays the current battery percentage, status (charging, discharging, full), estimated time remaining, and power source (plugged in or on battery). It features a clean, modern UI with a dark theme and animated progress bar.

## Features

*   **Real-time Battery Information:** Displays the current battery percentage, status, and estimated time remaining.
*   **Cross-Platform:** Works on Windows, macOS, and Linux (where `psutil` is supported).
*   **Dark Theme:** A modern, visually appealing dark theme.
*   **Animated Progress Bar:** Smoothly animated progress bar that changes color based on battery level.
*   **Custom Title Bar:**  Frameless window with a custom title bar and close button.
*   **Automatic Refresh:** Updates battery information automatically every 30 seconds.
*   **Manual Refresh:**  Includes a refresh button to manually update the information.
*   **Standalone Executable (Windows):**  Can be packaged into a single, easy-to-distribute executable using PyInstaller.
* **Error Handling:**

## Prerequisites

*   Python 3.7+
*   PySide6
*   psutil

## Installation and Running (Development)

1.  **Clone the Repository:**

    ```bash
    git clone <your_repository_url>
    cd <repository_directory>
    ```
    Replace `<your_repository_url>` and `<repository_directory>` with the actual URL and directory name.

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    *   **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate
        ```
    *   **Windows (PowerShell):**
        ```powershell
        . venv\Scripts\Activate.ps1
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Compile Resources:**

    ```bash
    .\build.bat  # Windows (PowerShell) - Preferred
    # OR
    build.bat    # Windows (cmd.exe)
    ```

6.  **Run the Application:**

    ```bash
    python -m src.battery_monitor.main
    ```

## Building a Standalone Executable (Windows)

This project uses PyInstaller to create a standalone executable.

1.  **Install PyInstaller (if you haven't already):**

    ```bash
     pip install pyinstaller
    ```
     Make sure you've completed steps 1-5 of Installation

2.  **Build the Executable:**
      ```bash
      pyinstaller --onefile --windowed --add-data "src/battery_monitor/resources;resources" --icon=src/battery_monitor/resources/refresh_icon.png src/battery_monitor/main.py
      ```
     Or use .spec file
     ```
     pyinstaller main.spec
     ```

3.  **Find the Executable:** The executable (`.exe` file) will be created in the `dist` subdirectory of your project. You can copy and distribute this executable.

## Project Structure
battery_monitor/
├── src/                  # Main source code directory
│   ├── battery_monitor/    # Python package for the application
│   │   ├── init.py   # Makes 'battery_monitor' a package
│   │   ├── main.py       # Main application entry point
│   │   ├── battery.py    # BatteryInfo class (logic separated)
│   │   ├── gui.py        # BatteryWindow and other UI components
│   │   ├── widgets.py    # CustomFrame, AnimatedProgressBar
│   │   └── resources.qrc # Qt resource file (for icons, etc.)
│   │   └── resources/    # Store resource files here
│   │   │     └── refresh_icon.png  # Example icon
│   ├── tests/            # Unit and integration tests
│   │   ├── init.py
│   │   ├── test_battery.py
│   │   └── test_gui.py     # (Optional, if you add GUI tests)
│   └── data           # Store the compiled resource file
│       └── resources_rc.py # Compiled Qt resource file
├── .gitignore            # Files and directories to ignore in Git
├── LICENSE               # Your software license (e.g., MIT, GPL)
├── README.md             # Project description, usage instructions
├── requirements.txt      # Project dependencies (for pip)
├── setup.py              # (Optional, for building/distributing as a package)
└── build.bat      # Windows Build Script


## Contributing

Contributions are welcome!  Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
