#!/usr/bin/env python3
import os
import subprocess
import sys
import time

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        from PyQt5.QtWidgets import QApplication
        return True
    except ImportError as e:
        print(f"Missing dependencies: {str(e)}")
        print("Please run install_gui_dependencies.py first")
        return False

def run_xvfb():
    """Start Xvfb if not running"""
    try:
        # Check if Xvfb is already running on display :1
        subprocess.run(
            "ps aux | grep 'Xvfb :1' | grep -v grep",
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        print("Xvfb is already running")
    except subprocess.CalledProcessError:
        # Start Xvfb
        print("Starting Xvfb...")
        subprocess.Popen(
            "Xvfb :1 -screen 0 1024x768x24",
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        time.sleep(1)  # Give Xvfb time to start

def run_gui():
    """Run the GUI application"""
    print("Starting RedTiger-style GUI...")
    os.environ["DISPLAY"] = ":1"
    subprocess.run(["python", "/workspaces/random/redtiger_style_gui.py"])

if __name__ == "__main__":
    if check_dependencies():
        run_xvfb()
        run_gui()
    else:
        print("Would you like to install the dependencies now? (y/n)")
        choice = input().lower()
        if choice == 'y':
            subprocess.run([sys.executable, "/workspaces/random/install_gui_dependencies.py"])
