import subprocess
import os
import requests
import platform
import psutil
import GPUtil
from datetime import datetime

version = "0.1.0"

def clear_console():
    if os.name == 'nt':
        os.system('cls')
        os.system('cls')  # Clear the buffer
    else:
        os.system('clear')
        os.system('clear')  # Clear the buffer

banner = rf"""
        ____           _                                                
       / __ \___  _  _( )_____ Multitools Version {version}                                         
      / / / / _ \| |/_/// ___/_  ___      ____  _ __              __    
     / /_/ /  __/>  <  (__  )  |/  /_  __/ / /_(_) /_____  ____  / /____
    /_____/\___/_/|_| /____/ /|_/ / / / / / __/ / __/ __ \/ __ \/ / ___/
                          / /  / / /_/ / / /_/ / /_/ /_/ / /_/ / (__  ) 
                         /_/  /_/\__,_/_/\__/_/\__/\____/\____/_/____/  
                         
    NOTE: None of your information is stored or shared with anyone else.
          If anyone sold you this software, ask for a refund immediatly; this is a free software.
          
          (Dont redistribute this software without permission from the author.)
"""
options = rf"""
        [1] IP Inspect
        [2] Device Specifications
        [3] Roblox Account Beamer (EXPERIMENTAL, use this for testing purposes only)
        [U] Check for updates
        [X] Exit
"""
    
def display_menu():
    clear_console()
    print(banner)
    print(options)
    
def inspect_ip():
    ip = input("Enter IP address to inspect (leave blank to use your public IP): ")
    
    if not ip:
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            ip = response.json().get("ip")
        else:
            print("Failed to retrieve your public IP address.")
            input("Press Enter to continue...")
            return
    
    response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 'success':
            print(f"IP: {data.get('query')}")
            print(f"Continent: {data.get('continent')}")
            print(f"Continent Code: {data.get('continentCode')}")
            print(f"Country: {data.get('country')}")
            print(f"Country Code: {data.get('countryCode')}")
            print(f"Region: {data.get('region')}")
            print(f"Region Name: {data.get('regionName')}")
            print(f"City: {data.get('city')}")
            print(f"District: {data.get('district')}")
            print(f"ZIP: {data.get('zip')}")
            print(f"Latitude: {data.get('lat')}")
            print(f"Longitude: {data.get('lon')}")
            print(f"Timezone: {data.get('timezone')}")
            print(f"Offset: {data.get('offset')}")
            print(f"Currency: {data.get('currency')}")
            print(f"ISP: {data.get('isp')}")
            print(f"Organization: {data.get('org')}")
            print(f"AS: {data.get('as')}")
            print(f"AS Name: {data.get('asname')}")
            print(f"Reverse DNS: {data.get('reverse')}")
            print(f"Mobile: {data.get('mobile')}")
            print(f"Proxy: {data.get('proxy')}")
            print(f"Hosting: {data.get('hosting')}")
            input("Press Enter to continue...")
        else:
            print(f"Error: {data.get('message')}")
            input("Press Enter to continue...")
    else:
        print("Failed to retrieve data.")
        input("Press Enter to continue...")

while True:
    display_menu()
    useroption = input("Select an option: ")

    if useroption == "u" or useroption == "U":
        clear_console()
        subprocess.run(["python3", "update.py"])
    elif useroption == "1":
        clear_console()
        print(banner)
        print("\033[92m        [1] IP Inspect\033[0m")  # Green text
        inspect_ip()
    elif useroption == "2":
        clear_console()
        print(banner)
        print("\033[92m        [2] Device Specifications\033[0m")
        print("--------------------------------")
        print("Device Specifications:")
        print("=" * 40)
        
        # System Information
        print("\n## System Information ##")
        print(f"System: {platform.system()}")
        print(f"Node Name: {platform.node()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Machine: {platform.machine()}")
        print(f"Processor: {platform.processor()}")
        print(f"Architecture: {platform.architecture()}")
        
        # CPU Information
        print("\n## CPU Information ##")
        print(f"CPU Count: {psutil.cpu_count(logical=True)}")
        cpu_freq = psutil.cpu_freq()
        if cpu_freq:
            print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")
            if cpu_freq.min:
                print(f"Minimum Frequency: {cpu_freq.min:.2f} MHz")
            if cpu_freq.max:
                print(f"Maximum Frequency: {cpu_freq.max:.2f} MHz")
        print(f"Physical cores: {psutil.cpu_count(logical=False)}")
        print(f"Total cores: {psutil.cpu_count(logical=True)}")
        print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
        
        # Per-core CPU usage
        print("\n## Per-core CPU Usage ##")
        for i, percentage in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
            print(f"Core {i}: {percentage}%")
        
        # Memory Information
        print("\n## Memory Information ##")
        print(f"Total Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
        print(f"Available Memory: {psutil.virtual_memory().available / (1024 ** 3):.2f} GB")
        print(f"Used Memory: {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
        print(f"Memory Usage: {psutil.virtual_memory().percent}%")
        
        # GPU Information
        print("\n## GPU Information ##")
        try:
            gpus = GPUtil.getGPUs()
            if gpus:
                for i, gpu in enumerate(gpus):
                    print(f"GPU {i+1}: {gpu.name}")
                    print(f"  Load: {gpu.load * 100:.2f}%")
                    print(f"  Free Memory: {gpu.memoryFree} MB")
                    print(f"  Used Memory: {gpu.memoryUsed} MB")
                    print(f"  Total Memory: {gpu.memoryTotal} MB")
                    print(f"  Temperature: {gpu.temperature} °C")
            else:
                print("No GPUs detected")
        except Exception as e:
            print(f"Could not retrieve GPU information: {e}")
        
        # Disk Information
        print("\n## Disk Information ##")
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                print(f"Device: {partition.device}")
                print(f"  Mountpoint: {partition.mountpoint}")
                print(f"  File system: {partition.fstype}")
                print(f"  Total Size: {usage.total / (1024 ** 3):.2f} GB")
                print(f"  Used: {usage.used / (1024 ** 3):.2f} GB")
                print(f"  Free: {usage.free / (1024 ** 3):.2f} GB")
                print(f"  Usage: {usage.percent}%")
            except PermissionError:
                print(f"Device: {partition.device} - Access denied")
        
        # System Uptime
        try:
            boot_time = psutil.boot_time()
            boot_datetime = datetime.fromtimestamp(boot_time)
            uptime = datetime.now() - boot_datetime
            print(f"\nSystem Uptime: {uptime.days} days, {uptime.seconds//3600} hours, {(uptime.seconds//60)%60} minutes")
        except Exception as e:
            print(f"\nCould not determine system uptime: {e}")
        
        # Battery Information
        print("\n## Battery Information ##")
        battery = psutil.sensors_battery()
        if battery:
            print(f"Battery percentage: {battery.percent}%")
            print(f"Power plugged in: {'Yes' if battery.power_plugged else 'No'}")
            if battery.secsleft != -1:
                minutes, seconds = divmod(battery.secsleft, 60)
                hours, minutes = divmod(minutes, 60)
                print(f"Battery time left: {hours}h {minutes}m")
        else:
            print("No battery detected")
        
        input("Press Enter to continue...")
    elif useroption == "x" or useroption == "X":
        clear_console()
        print("Exiting to console.")
        break
    else:
        clear_console()
        print(banner)
        print("Invalid option selected.")
        input("Press Enter to continue...")
