# the-comic-virus
💻 System Killer – A harmless prank for your friends
System Killer is a playful Python script that simulates a fake system deletion process. When executed, it opens a fullscreen terminal, floods the screen with red random characters, displays fake system information, shows a progress bar, and finally asks the user whether they really want to delete the system. If they answer "y", the computer politely shuts down after 3 seconds (or you can replace that with a funny image).

⚠️ No actual harm is done – no files are deleted, no system settings are changed. It's just a visual joke.

✨ Features
Fullscreen terminal – the console window is maximized and cannot be closed easily (Ctrl+C, Alt+F4 are blocked).

Red random characters – for 30 seconds, a stream of random characters fills the screen, creating a "hacking" atmosphere.

Fake system info – displays hostname, OS version, architecture, and (if psutil is installed) CPU cores, RAM usage, and disk usage.

Progress bar – simulates "deleting system files".

Interactive question – repeatedly asks y/n until the user enters y.

Shutdown punchline – after pressing y, the computer shuts down after 3 seconds (or you can customize it to show a fullscreen image instead).

Blocked termination – prevents closing the console via the close button or keyboard shortcuts.

🧠 How it works
When launched, the console immediately goes fullscreen and blocks all attempts to close it.

A 30‑second stream of red random characters is printed (simulating a system scan).

The screen clears and a fake "SYSTEM KILLER" banner appears, followed by some system information (gathered via platform and optionally psutil).

A progress bar runs for 5 seconds, pretending to delete files.

The program then asks:
Are you sure you want to completely delete the system? (y/n)

If the user types n, the question repeats.

If the user types y, the screen clears, a message "SYSTEM SHUTDOWN INITIATED" appears, and after 2 seconds the computer shuts down (3‑second countdown).

(Optional) If you prefer an image instead of shutdown, you can uncomment the show_image_protected function and include a PNG.

📦 Libraries used
Standard library modules:
os, sys, time, random, platform, threading, ctypes (for console manipulation)

Optional but recommended:

psutil – for detailed system info (CPU, RAM, disk). If not installed, the script shows basic info only.

Pillow – only needed if you want to display a fullscreen PNG image instead of shutting down.

All other functionality works out‑of‑the‑box with Python 3.6+ on Windows.

🚀 Installation & Usage
Option 1: Run from source
Make sure you have Python 3.6 or newer installed.

Clone this repository or download roflan.py.

(Optional) Install extra libraries for better system info / image support:

bash
pip install psutil pillow
Run the script:

bash
python roflan.py
Option 2: Run the compiled EXE (no Python required)
Download the latest roflan.exe from the Releases page.

Double‑click the EXE – the prank starts immediately.

To stop the prank before shutdown, you can force‑close the terminal via Task Manager (but it's designed to resist normal closing).

⚠️ Disclaimer
This program is a joke. It does NOT delete any files, does NOT harm your system, and does NOT collect any personal data.
The shutdown command is the standard Windows shutdown (shutdown /s /t 3) which can be cancelled by running shutdown /a in a command prompt within 3 seconds. Use it responsibly and only on computers where you have permission to prank.


