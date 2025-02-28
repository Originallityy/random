import tkinter as tk
import psutil
import os
import time

def update_monitor():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    memory_label.config(text=f"Memory Usage: {memory_usage}%")
    
    window.after(1000, update_monitor)  # Update every 1000ms (1 second)

# Check if a display is available
if 'DISPLAY' in os.environ:
    # Create the main window
    window = tk.Tk()
    window.title("Resource Monitor")
    window.geometry("400x300")  # Set initial window size

    # --- Styling ---
    bg_color = "#2b2b2b"  # Dark background
    fg_color = "white"    # Light text
    font = ("Arial", 12)

    window.configure(bg=bg_color)

    # --- Title Bar ---
    title_bar = tk.Frame(window, bg="#333333", height=30)
    title_bar.pack(fill="x")

    title_label = tk.Label(title_bar, text="Resource Monitor", fg=fg_color, bg="#333333", font=("Arial", 10))
    title_label.pack(side="left", padx=10)

    # --- Content Area ---
    content_frame = tk.Frame(window, bg=bg_color)
    content_frame.pack(fill="both", expand=True)

    # Create labels for CPU and memory usage
    cpu_label = tk.Label(content_frame, text="CPU Usage: N/A", fg=fg_color, bg=bg_color, font=font)
    cpu_label.pack(pady=10)

    memory_label = tk.Label(content_frame, text="Memory Usage: N/A", fg=fg_color, bg=bg_color, font=font)
    memory_label.pack(pady=10)

    # Start updating the monitor
    update_monitor()

    # Start the Tkinter main loop
    window.mainloop()
else:
    print("No display environment found. GUI cannot be started.")
    print("Displaying CPU and Memory usage in terminal instead.")
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage over 1 second
        memory_data = psutil.virtual_memory()
        memory_usage = memory_data.percent
        memory_total = memory_data.total / (1024 * 1024)  # in MB
        memory_available = memory_data.available / (1024 * 1024)  # in MB
        
        output = f"\rCPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}% (Total: {memory_total:.2f} MB, Available: {memory_available:.2f} MB)"
        print(output, end="")  # Use end="" to prevent newline
        time.sleep(1)
