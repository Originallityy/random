#!/usr/bin/env python3
import os
import subprocess
import sys
import time

def run_command(command, show_output=True):
    """Run a shell command and optionally print output"""
    print(f"Running: {command}")
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    
    if show_output:
        if stdout:
            print(f"Output: {stdout.decode()}")
        if stderr:
            print(f"Error: {stderr.decode()}")
    
    return process.returncode

def setup_terminal_gui():
    """Setup a terminal-based GUI alternative"""
    print("Setting up a terminal-based interface instead...")
    print("This doesn't require any additional dependencies")
    
    # Ask if user wants to run the terminal app now
    choice = input("\nDo you want to run the terminal application now? (y/n): ")
    if choice.lower() == 'y':
        subprocess.run(["python", "/workspaces/random/stand-alone.py"])
    
    return True

def main():
    print("Quick setup for GUI applications")
    print("Would you prefer: \n1. Try setting up the PyQt GUI (might take longer)\n2. Use the terminal application (immediate)")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "2":
        return setup_terminal_gui()
    
    try:
        # Check if we can import PyQt5 already
        print("Checking if PyQt5 is already installed...")
        try:
            import PyQt5
            print("PyQt5 is already installed!")
            has_pyqt = True
        except ImportError:
            print("PyQt5 not found, will need to install it.")
            has_pyqt = False
        
        if not has_pyqt:
            print("Installing PyQt5 (this might take a few minutes)...")
            run_command(f"{sys.executable} -m pip install PyQt5", show_output=False)
        
        # Start virtual X server
        print("Starting virtual display...")
        run_command("Xvfb :1 -screen 0 1024x768x24 -ac &", show_output=True)
        os.environ["DISPLAY"] = ":1"
        time.sleep(2)  # Give it a moment to start
        
        print("\nSetup complete! Running the GUI application...")
        run_command("python /workspaces/random/redtiger_style_gui.py")
        
        return True
    
    except Exception as e:
        print(f"Error during setup: {e}")
        print("\nWould you like to try the terminal-based application instead? (y/n)")
        choice = input().lower()
        if choice == 'y':
            return setup_terminal_gui()
    
    return False

if __name__ == "__main__":
    success = main()
    if not success:
        print("Setup failed. You can try running the terminal app with:")
        print("python /workspaces/random/stand-alone.py")
