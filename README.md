# KeyLoggerPlus--EmailAndPassword
This project is a Windows keylogger script written in Python that logs keystrokes, detects sensitive information like email addresses and potential passwords, and stores them in a text file. The script can be converted to an executable and set to auto-start on boot for background logging. It’s for educational purposes only.
## Features

- Logs keystrokes to a file located at:
  - `C:\Users\<username>\Documents\Keylogs.txt`
- Automatically differentiates:
  - **Email addresses**
  - **Potential passwords**
- Can be converted into an `.exe` file for easier deployment.
- Option to auto-start on system boot.

---

## Prerequisites

1. Install **Python 3.x** on your system.
2. Install required Python libraries using the following command:
   ```bash
   pip install pynput pygetwindow













Here’s the **corrected and streamlined guide**, including steps to handle errors with environment variables for auto-start.

---

### **1. Directory Structure**
Here’s the directory structure you should have for the GitHub repository:

```
Keylogger/
├── keylogger.py         # The Python script for the keylogger
├── README.md            # Project documentation
├── LICENSE              # License file (optional)
├── requirements.txt     # Python dependencies
└── screenshots/         # (Optional) Demo images
    ├── demo1.png
    ├── demo2.png
```

---

### **2. README File**
Your `README.md` file should explain the project. Here’s a detailed example:

```markdown
# Windows Keylogger

This is a Python-based Windows keylogger designed for educational purposes. It logs keystrokes and identifies sensitive information like email addresses and potential passwords using pattern matching. The keylogger runs in the background and can optionally be converted into an executable that runs on system startup.

---

## Features

- Logs keystrokes to a file located at:
  - `C:\Users\<username>\Documents\Keylogs.txt`
- Automatically differentiates:
  - **Email addresses**
  - **Potential passwords**
- Can be converted into an `.exe` file for easier deployment.
- Option to auto-start on system boot.

---

## Prerequisites

1. Install **Python 3.x** on your system.
2. Install required Python libraries using the following command:
   ```bash
   pip install pynput pygetwindow
   ```
3. Install **PyInstaller** to convert the script into an `.exe` file (optional):
   ```bash
   pip install pyinstaller
   ```

---

## Steps to Run

### 1. Running the Script
1. Clone the repository or download the `keylogger.py` file.
2. Open a terminal or Command Prompt in the directory where `keylogger.py` is located.
3. Run the script:
   ```bash
   python keylogger.py
   ```

The logs will be saved to the `Keylogs.txt` file in the `Documents` folder of the current user.

---

### 2. Converting to an Executable (Optional)
To run the keylogger without Python installed, convert it into an `.exe` file:

1. Open a terminal or Command Prompt in the folder containing `keylogger.py`.
2. Run the following command:
   ```bash
   pyinstaller --onefile --noconsole keylogger.py
   ```
3. After the build process completes, locate the executable in the `dist/` folder.
4. Move the `keylogger.exe` file to your project directory or another location.

---

### 3. Setting the EXE to Auto-Run on Boot
To make the keylogger start automatically when Windows boots:

#### Option 1: Add to the Startup Folder
1. Press `Win + R`, type `shell:startup`, and hit **Enter**.
2. Copy the `keylogger.exe` file into this folder.
3. The keylogger will now auto-run on boot.

#### Option 2: Modify the Windows Registry
1. Press `Win + R`, type `regedit`, and press **Enter**.
2. Navigate to the registry path:
   ```
   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
   ```
3. Right-click in the right-hand pane and select **New > String Value**.
4. Name the value something like `Keylogger`.
5. Double-click the new entry and set its value to the full path of `keylogger.exe`, for example:
   ```
   C:\Path\To\keylogger.exe
   ```
6. Close the Registry Editor.

## Error Handling

### Common Issues
1. **EXE does not auto-start on boot**:
   - Ensure the path in the Windows Registry is correct and points to `keylogger.exe`.
   - Check if the `.exe` file has sufficient permissions to run.
   - Verify that antivirus software has not blocked or deleted the executable.

2. **Missing Dependencies**:
   - Make sure to run:
     ```bash
     pip install -r requirements.txt
     ```





