import os
import time
import win32gui
import win32process
import psutil
import shutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OBS_FOLDER = os.getenv("OBS_FOLDER")
SECONDS_THRESHOLD = 10  # Only rename files created in the last 10 seconds
WAIT_TIME = 5  # Wait for 5 seconds before renaming and moving the file

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
    print(f"Monitoring OBS folder at {OBS_FOLDER}...")
    last_renamed_file = None
    while True:
        time.sleep(1)  # Wait for a second

        files = os.listdir(OBS_FOLDER)
        files = [f for f in files if f.endswith('.mp4')]  # Change this to match your files
        if not files:
            continue

        # Get the latest file
        latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(OBS_FOLDER, f)))

        # If the latest file is the same as the last one we renamed, skip it
        if latest_file == last_renamed_file:
            continue

        # Check if the latest file was created in the last SECONDS_THRESHOLD seconds
        creation_time = os.path.getctime(os.path.join(OBS_FOLDER, latest_file))
        if time.time() - creation_time > SECONDS_THRESHOLD:
            continue

        # Get the name of the active window's process
        process_name = get_active_window_process_name()
        if process_name:
            # Create a new folder with the process name, if it doesn't exist
            new_folder = os.path.join(OBS_FOLDER, process_name)
            os.makedirs(new_folder, exist_ok=True)

            # Wait for a bit before renaming and moving the file
            time.sleep(WAIT_TIME)

            # Move and rename the file
            new_name = f"{process_name}_{latest_file}"
            shutil.move(os.path.join(OBS_FOLDER, latest_file), os.path.join(new_folder, new_name))

            # Print a message indicating that a file was renamed and moved
            print(f"Renamed and moved {latest_file} to {os.path.join(new_folder, new_name)}")

        # Update the last renamed file
        last_renamed_file = new_name

if __name__ == "__main__":
    rename_files()
