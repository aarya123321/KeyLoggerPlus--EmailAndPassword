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
