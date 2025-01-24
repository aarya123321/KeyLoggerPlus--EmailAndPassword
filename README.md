


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

   ```
3. Install **PyInstaller** to convert the script into an `.exe` file (optional):
   ```bash
   pip install pyinstaller
   ```

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
     
Working:
Here i just opened Text editor for testing purpose ,it can be anywhere on the pc if someone types anything it will get recoreded and if its email and passowrd it will get tagged in most cases.

![image](https://github.com/user-attachments/assets/2f9e0805-4697-405e-b589-76ead2224332)

https://github.com/user-attachments/assets/83166b45-fe04-42d0-bb81-639a13d75818

## Troubleshooting PyInstaller Installation

If you see the error `'pyinstaller' is not recognized as an internal or external command`, follow these steps:

1. Install `PyInstaller` using the following command:
   ```bash
   pip install pyinstaller
   ```

2. If the error persists, make sure your Python `Scripts` directory is added to the system `PATH`. Here's how to add it:

   - Find your Python Scripts folder (usually in `C:\Users\<YourUsername>\AppData\Local\Programs\Python\PythonXY\Scripts`).
   - Add it to the system `PATH` environment variable.

3. **Add Python Scripts to the System Path (if needed):**
   If you still get the error after installing `PyInstaller`, the Python scripts folder might not be added to your system's PATH.

   - Find the location of your Python installation. For example, it’s often located in `C:\Users\<YourUsername>\AppData\Local\Programs\Python\PythonXY\Scripts` on Windows (where `XY` is your Python version, like `39` for Python 3.9).
   - Copy the path to the `Scripts` folder.
   - To add this to your PATH on Windows, follow these steps:
     1. Right-click on **This PC** or **My Computer** and select **Properties**.
     2. Click on **Advanced system settings** on the left panel.
     3. Click on the **Environment Variables** button.
     4. Under **System variables**, find and select the **Path** variable, then click **Edit**.
     5. In the **Edit Environment Variable** window, click **New** and paste the copied path (e.g., `C:\Users\<YourUsername>\AppData\Local\Programs\Python\PythonXY\Scripts`).
     6. Click **OK** to save the changes.

4. **Restart Your Command Prompt:**
   After adding the path to your environment variables, restart your command prompt or terminal to apply the changes.

5. **Test Again:**
   Now try running the `pyinstaller` command again:

   ```bash
   pyinstaller --onefile --noconsole keylogger.py
   ```

   It should work without the `'pyinstaller' is not recognized as an internal or external command` error.

# DISCLAIMER

**IMPORTANT**: This project is intended for educational purposes only. Misuse of the code for unauthorized access to computer systems, accounts, or networks is illegal and unethical. By using this project, you agree that you are solely responsible for your actions and that the author is not liable for any legal consequences.




