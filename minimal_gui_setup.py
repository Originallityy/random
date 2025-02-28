#!/usr/bin/env python3
import subprocess
import sys
import os
import time

def run_command(cmd, show_output=True):
    """Run a command and optionally show its output"""
    print(f"Running: {cmd}")
    process = subprocess.Popen(
        cmd, 
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    
    if show_output:
        if stdout:
            print(stdout.decode())
        if stderr:
            print(stderr.decode())
    
    return process.returncode

def is_command_available(command):
    """Check if a command is available in the system"""
    try:
        subprocess.run(
            f"command -v {command}",
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return True
    except subprocess.CalledProcessError:
        return False

def install_minimal_deps():
    """Install minimal dependencies without full X server"""
    print("Installing minimal dependencies...")
    
    # Try to install just PyQt5 first
    run_command(f"{sys.executable} -m pip install PyQt5")
    
    # If xvfb is available, we can use it
    if is_command_available("Xvfb"):
        print("Xvfb is already available")
    else:
        print("Xvfb not found. Trying to install it...")
        run_command("sudo apt-get update -y && sudo apt-get install -y xvfb")

def main():
    print("Minimal GUI Setup")
    print("This script will attempt to set up the minimum required dependencies.")
    
    choice = input("Continue with setup? (y/n): ")
    if choice.lower() != 'y':
        print("Setup cancelled. You can run the terminal app instead:")
        print("python /workspaces/random/stand-alone.py")
        return
    
    # First, install minimal dependencies
    install_minimal_deps()
    
    # Try to set up a minimal X server
    print("\nTrying to set up a minimal X server...")
    run_command("Xvfb :1 -screen 0 800x600x16 &")
    os.environ["DISPLAY"] = ":1"
    
    # Give Xvfb time to start
    print("Waiting for X server to start...")
    time.sleep(3)
    
    # Check if display is working
    print("\nTesting display configuration:")
    display_test = run_command("xdpyinfo -display :1", show_output=False)
    
    if display_test == 0:
        print("Display is working!")
        print("\nStarting PyQt application...")
        run_command(f"{sys.executable} /workspaces/random/redtiger_style_gui.py")
    else:
        print("Display setup failed. Falling back to terminal application.")
        run_command(f"{sys.executable} /workspaces/random/stand-alone.py")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSetup interrupted. You can run the terminal app instead:")
        print("python /workspaces/random/stand-alone.py")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("You can run the terminal app instead:")
        print("python /workspaces/random/stand-alone.py")
