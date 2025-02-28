import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QLabel, QStackedWidget, 
                            QFrame, QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QPoint
from PyQt5.QtGui import QFont, QIcon, QColor, QPalette

class TitleBar(QWidget):
    """Custom title bar class"""
    close_clicked = pyqtSignal()
    minimize_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(TitleBar, self).__init__(parent)
        self.setAutoFillBackground(True)
        
        # Set background color for title bar
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#1e1e1e"))
        self.setPalette(palette)
        
        self.setMinimumHeight(30)
        self.setMaximumHeight(30)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Title label
        self.title = QLabel("RedTiger-Style Application")
        self.title.setStyleSheet("color: white; font-size: 12px; font-weight: bold;")
        self.title.setAlignment(Qt.AlignCenter)
        
        # Close and Minimize buttons
        self.minimize_btn = QPushButton("−")
        self.minimize_btn.setFixedSize(30, 30)
        self.minimize_btn.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: #1e1e1e;
                border: none;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
        """)
        
        self.close_btn = QPushButton("×")
        self.close_btn.setFixedSize(30, 30)
        self.close_btn.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: #1e1e1e;
                border: none;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        
        # Connect signals
        self.close_btn.clicked.connect(self.close_clicked)
        self.minimize_btn.clicked.connect(self.minimize_clicked)
        
        # Add empty label for left side spacing
        spacer = QLabel()
        layout.addWidget(spacer)
        layout.addWidget(self.title)
        layout.addWidget(self.minimize_btn)
        layout.addWidget(self.close_btn)
        
        # Make title bar draggable
        self.start = QPoint(0, 0)
        self.pressing = False
    
    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True
    
    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent().window().move(self.mapToGlobal(self.movement))
            self.start = self.end
    
    def mouseReleaseEvent(self, event):
        self.pressing = False

class SidebarButton(QPushButton):
    """Custom button class for sidebar"""
    def __init__(self, text, icon_path=None, parent=None):
        super(SidebarButton, self).__init__(text, parent)
        self.setMinimumHeight(40)
        self.setFont(QFont("Arial", 10))
        
        # Styling
        self.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: #1e1e1e;
                border: none;
                text-align: left;
                padding-left: 15px;
            }
            QPushButton:hover {
                background-color: #2d2d2d;
            }
            QPushButton:pressed {
                background-color: #007acc;
            }
        """)
        
        # Set icon if provided
        if icon_path and os.path.exists(icon_path):
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(20, 20))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(800, 600)
        
        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.setCentralWidget(main_widget)
        
        # Custom title bar
        self.title_bar = TitleBar(self)
        self.title_bar.close_clicked.connect(self.close)
        self.title_bar.minimize_clicked.connect(self.showMinimized)
        main_layout.addWidget(self.title_bar)
        
        # Content area
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        main_layout.addWidget(content_widget)
        
        # Sidebar
        sidebar = QWidget()
        sidebar.setMinimumWidth(200)
        sidebar.setMaximumWidth(200)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        # Create sidebar buttons
        tools = [
            "Dashboard", "IP Inspect", "Device Specifications", 
            "Roblox Account Lookup", "Network Tools", "Settings"
        ]
        
        self.tool_buttons = []
        for tool in tools:
            btn = SidebarButton(tool)
            sidebar_layout.addWidget(btn)
            self.tool_buttons.append(btn)
        
        # Add stretch to push buttons to the top
        sidebar_layout.addStretch()
        
        # Main content area with stacked widget
        self.content_stack = QStackedWidget()
        
        # Create pages for each tool
        self.create_pages()
        
        # Connect button signals
        for i, btn in enumerate(self.tool_buttons):
            btn.clicked.connect(lambda checked, index=i: self.content_stack.setCurrentIndex(index))
        
        # Add sidebar and content stack to the layout
        content_layout.addWidget(sidebar)
        content_layout.addWidget(self.content_stack)
        
        # Set the style for the whole application
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
            QWidget {
                background-color: #121212;
                color: white;
            }
            QScrollArea {
                border: none;
            }
        """)
    
    def create_pages(self):
        # Dashboard page
        dashboard = QWidget()
        dashboard_layout = QVBoxLayout(dashboard)
        dashboard_layout.addWidget(QLabel("Dashboard Content"))
        self.content_stack.addWidget(dashboard)
        
        # IP Inspect page
        ip_inspect = QWidget()
        ip_layout = QVBoxLayout(ip_inspect)
        ip_layout.addWidget(QLabel("IP Inspect Tool"))
        self.content_stack.addWidget(ip_inspect)
        
        # Device Specifications page
        device_specs = QWidget()
        device_layout = QVBoxLayout(device_specs)
        device_layout.addWidget(QLabel("Device Specifications"))
        self.content_stack.addWidget(device_specs)
        
        # Roblox Account Lookup page
        roblox = QWidget()
        roblox_layout = QVBoxLayout(roblox)
        roblox_layout.addWidget(QLabel("Roblox Account Lookup"))
        self.content_stack.addWidget(roblox)
        
        # Network Tools page
        network = QWidget()
        network_layout = QVBoxLayout(network)
        network_layout.addWidget(QLabel("Network Tools"))
        self.content_stack.addWidget(network)
        
        # Settings page
        settings = QWidget()
        settings_layout = QVBoxLayout(settings)
        settings_layout.addWidget(QLabel("Settings"))
        self.content_stack.addWidget(settings)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
