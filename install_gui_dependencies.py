#!/usr/bin/env python3
import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and print output"""
    print(f"Running: {command}")
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    
    if stdout:
        print(f"Output: {stdout.decode()}")
    if stderr:
        print(f"Error: {stderr.decode()}")
    
    return process.returncode

def install_linux_dependencies():
    """Install required Linux packages for PyQt5 and OpenGL"""
    print("Installing required system packages for PyQt5 and OpenGL...")
    
    # Update package list
    run_command("sudo apt-get update -y")
    
    # Install required packages for PyQt5 and OpenGL
    packages = [
        "libgl1-mesa-glx",  # OpenGL libraries
        "libegl1-mesa",     # EGL libraries
        "libxkbcommon-x11-0",  # X11 keyboard handling
        "libxcb-icccm4",    # X11 protocols
        "libxcb-image0",
        "libxcb-keysyms1",
        "libxcb-randr0",
        "libxcb-render-util0",
        "libxcb-xkb1",
        "libxcb-shape0",
        "libfontconfig1",   # Font management
        "libdbus-1-3",      # D-Bus for inter-process communication
        "xvfb"              # Virtual framebuffer X server
    ]
    
    run_command(f"sudo apt-get install -y {' '.join(packages)}")

def install_python_packages():
    """Install required Python packages"""
    print("Installing required Python packages...")
    packages = [
        "PyQt5",
        "PyQt5-sip"
    ]
    run_command(f"{sys.executable} -m pip install --upgrade {' '.join(packages)}")

def setup_xvfb():
    """Configure Xvfb as a virtual display"""
    print("Setting up Xvfb virtual display...")
    
    # Start Xvfb on display :1
    run_command("Xvfb :1 -screen 0 1024x768x24 &")
    
    # Set the DISPLAY environment variable
    os.environ["DISPLAY"] = ":1"
    print("DISPLAY environment variable set to :1")

def main():
    print("Installing dependencies for PyQt5 GUI applications...")
    
    install_linux_dependencies()
    install_python_packages()
    setup_xvfb()
    
    print("\nSetup complete! You can now run your PyQt5 application with:")
    print("DISPLAY=:1 python /workspaces/random/redtiger_style_gui.py")
    print("\nAlternatively, you can run it directly with:")
    print("python /workspaces/random/redtiger_style_gui.py")
    
    # Ask if user wants to run the GUI app now
    choice = input("\nDo you want to run the RedTiger-style GUI now? (y/n): ")
    if choice.lower() == 'y':
        run_command("python /workspaces/random/redtiger_style_gui.py")

if __name__ == "__main__":
    main()
