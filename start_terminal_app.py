#!/usr/bin/env python3
import os
import subprocess
import sys

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear_console()
    print("""
    ╔════════════════════════════════════════════════╗
    ║                                                ║
    ║               MULTI-TOOLS LAUNCHER             ║
    ║                                                ║
    ╚════════════════════════════════════════════════╝
    
    The terminal-based application doesn't require any graphical display
    and works on all systems with Python.
    
    Starting terminal application...
    """)
    
    # Small delay to let the user read the message
    import time
    time.sleep(2)
    
    # Start the terminal application
    try:
        subprocess.run([sys.executable, "/workspaces/random/stand-alone.py"])
    except Exception as e:
        print(f"Error running the application: {e}")
        print("Press Enter to exit...")
        input()

if __name__ == "__main__":
    main()
