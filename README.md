# coviPing - COVID-19 Status Notifier via Windows Notification

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A simple Python script that provides periodic desktop notifications on Windows with the latest global COVID-19 statistics. The script runs silently in the background and fetches live data to keep you informed.

---

## Screenshot

<img src="https://github.com/user-attachments/assets/fb018201-d44f-46cf-b840-cee6379d08a1" alt="gif-preview" />

## Features
- Live Data: Fetches up-to-date global case numbers from a reliable API.
- Background Operation: Runs silently on startup without any intrusive console windows.
- Customizable: Easily change the notification frequency by editing a single variable.
- Lightweight: Minimal dependencies and low resource usage.

## Requirements
```
requests==2.32.4
win10toast==0.9
```

## Usage

To run the application on-demand, simply execute the coviPing.py script from the root directory: ```python coviPing.py```

To run the application automatically and silently:
- Edit the ```coviPing.exe.vbs``` file in notepad, choose the correct path, then copy the vbs file to startup folder as such,
  ```
      Win + R to open "Run" systems app. OR search for "Run" on Start Menu Search Functionality.
      Type "shell:startup" and hit enter to open the startup folder. Generally located at C:\Users\SubhojitGhimire\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
  ```

<h1></h1>

**This README.md file has been improved for overall readability (grammar, sentence structure, and organization) using AI tools.*
