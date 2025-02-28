import sys
import os
import platform
import psutil
import requests
import time
import threading
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QLabel, QStackedWidget, 
                            QFrame, QScrollArea, QSizePolicy, QLineEdit, 
                            QTextEdit, QProgressBar, QGridLayout, QComboBox)
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QPoint, QThread, pyqtSlot
from PyQt5.QtGui import QFont, QIcon, QColor, QPalette

class WorkerThread(QThread):
    """Worker thread for background tasks"""
    update_signal = pyqtSignal(dict)
    
    def __init__(self, task_type, params=None):
        super().__init__()
        self.task_type = task_type
        self.params = params if params else {}
        self.running = True
    
    def run(self):
        if self.task_type == "system_monitor":
            self.run_system_monitor()
        elif self.task_type == "ip_lookup":
            self.run_ip_lookup()
    
    def stop(self):
        self.running = False
        self.wait()
    
    def run_system_monitor(self):
        """Continuously monitor system resources"""
        while self.running:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            # Get per-core CPU usage
            per_core = psutil.cpu_percent(interval=1, percpu=True)
            
            # Get disk usage
            disk_usage = {}
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disk_usage[partition.mountpoint] = {
                        "total": usage.total,
                        "used": usage.used,
                        "free": usage.free,
                        "percent": usage.percent
                    }
                except:
                    pass
            
            data = {
                "cpu": cpu_usage,
                "per_core": per_core,
                "memory": {
                    "total": memory.total,
                    "available": memory.available,
                    "used": memory.used,
                    "percent": memory.percent
                },
                "disk": disk_usage
            }
            
            self.update_signal.emit(data)
            time.sleep(1)
    
    def run_ip_lookup(self):
        """Perform IP lookup"""
        ip = self.params.get("ip", "")
        
        if not ip:
            try:
                response = requests.get("https://api.ipify.org?format=json", timeout=5)
                if response.status_code == 200:
                    ip = response.json().get("ip")
                else:
                    self.update_signal.emit({"error": "Failed to get your IP address"})
                    return
            except Exception as e:
                self.update_signal.emit({"error": f"Network error: {str(e)}"})
                return
        
        try:
            response = requests.get(
                f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query",
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    self.update_signal.emit({"ip_data": data})
                else:
                    self.update_signal.emit({"error": data.get('message', 'Unknown error')})
            else:
                self.update_signal.emit({"error": f"API returned status code {response.status_code}"})
                
        except Exception as e:
            self.update_signal.emit({"error": f"Error during lookup: {str(e)}"})

class TitleBar(QWidget):
    """Custom title bar class"""
    close_clicked = pyqtSignal()
    minimize_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(TitleBar, self).__init__(parent)
        # ... (same implementation as before)

class SidebarButton(QPushButton):
    """Custom button class for sidebar"""
    def __init__(self, text, icon_path=None, parent=None):
        super(SidebarButton, self).__init__(text, parent)
        # ... (same implementation as before)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(900, 650)
        self.worker_threads = []
        
        # Main widget and layout setup
        # ... (similar structure as before)
        
        # Create CPU and RAM monitors
        self.setup_dashboard()
        
        # Setup IP Inspect page
        self.setup_ip_inspector()
        
        # Setup Device Specifications page
        self.setup_device_specs()

    def setup_dashboard(self):
        # Implementation details for dashboard with real-time monitoring
        pass
    
    def setup_ip_inspector(self):
        # Implementation details for IP lookup tool
        pass
    
    def setup_device_specs(self):
        # Implementation details for device specifications
        pass
    
    # Add other method implementations
    
    def closeEvent(self, event):
        # Stop all worker threads before closing
        for thread in self.worker_threads:
            thread.stop()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
