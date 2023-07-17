import os
import time
import win32gui
import win32process
import psutil
import shutil

OBS_FOLDER = "path_to_your_OBS_folder"
SECONDS_THRESHOLD = 5  # Only rename files created in the last 10 seconds

def get_active_window_process_name():
    """Get the name of the process for the active window."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        return psutil.Process(pid).name()
    except Exception:
        return None

def rename_files():
    """Monitor the OBS folder and rename the latest file."""
    while True:
        time.sleep(1)  # Wait for a second

        files = os.listdir(OBS_FOLDER)
        files = [f for f in files if f.endswith('.mp4')]  # Change this to match your files
        if not files:
            continue

        # Get the latest file
        latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(OBS_FOLDER, f)))

        # Check if the latest file was created in the last SECONDS_THRESHOLD seconds
        creation_time = os.path.getctime(os.path.join(OBS_FOLDER, latest_file))
        if time.time() - creation_time > SECONDS_THRESHOLD:
            continue

        # Get the name of the active window's process
        process_name = get_active_window_process_name()
        if process_name:
            new_name = f"{process_name}_{latest_file}"
            shutil.move(os.path.join(OBS_FOLDER, latest_file), os.path.join(OBS_FOLDER, new_name))

if __name__ == "__main__":
    rename_files()
