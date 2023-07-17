# 🎮 OBS File Renamer

This Python script monitors a specified folder for new video files (like those created by OBS Replay Buffer) and renames the latest file to include the name of the currently active window's process. This is useful for situations where you are recording gameplay from different games and want the output files to be automatically named according to the game that was being recorded.

# 🚀 Simple Usage

1. Download the latest release from the [Releases](https://github.com/Nordikk/obs-file-renamer/releases)

2. Create a .env file in the same directory as your script with the following content:

```bash
OBS_FOLDER=path_to_your_OBS_folder
```

3. Launch `obs_file_renamer.exe`.


# 🧑‍🔬 Advanced Usage

## 🛠️ Requirements

This script requires Python 3.6 or higher, along with the following Python packages:

- `pywin32==300`
- `psutil==5.8.0`
- `python-dotenv==0.19.2`

These packages can be installed using pip:

```bash
pip install -r requirements.txt
```

## 💻 Usage

First, create a .env file in the same directory as your script with the following content:

```bash
OBS_FOLDER=path_to_your_OBS_folder
```

Then, adjust the SECONDS_THRESHOLD variable in the script to match your setup. SECONDS_THRESHOLD is the number of seconds within which a file should have been created in order to be renamed. This prevents the script from renaming older files.

To run the script, simply execute it with Python:

````bash
python obs_file_renamer.py
````

The script will continuously monitor the OBS_FOLDER for new files and rename the latest file with the name of the active window's process.

## ⚠️ Disclaimer
Please be aware that the script might not work perfectly for all applications. Some applications might not set their window title to the name of the game, or they might have multiple windows open. You may need to adjust the script to fit your specific use case. Also, be aware that this script has the potential to access sensitive information, as it reads the title of the currently active window.
