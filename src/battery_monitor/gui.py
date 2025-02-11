# src/battery_monitor/gui.py

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QFrame,
                             QProgressBar, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QColor, QIcon

# Change these lines:
from battery_monitor.battery import BatteryInfo  # Absolute import
from battery_monitor.widgets import CustomFrame, AnimatedProgressBar  # Absolute import
from battery_monitor.data import resources_rc  # Absolute import


class BatteryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ... (rest of your BatteryWindow code) ...
        self.setWindowTitle("Battery Health Monitor")
        self.setMinimumSize(500, 700)

        # Set window flags for a modern look
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QWidget#centralWidget {
                background-color: #1a1a1a;
                border-radius: 20px;
                border: 1px solid #2d2d2d;
            }
            QPushButton {
                background-color: #0078d4;
                border: none;
                color: white;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1e90ff;
            }
            QPushButton:pressed {
                background-color: #005fb3;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
            QProgressBar {
                border: 2px solid #2d2d2d;
                border-radius: 8px;
                text-align: center;
                background-color: #1a1a1a;
                height: 25px;
            }
            QProgressBar::chunk {
                border-radius: 6px;
            }
        """)

        # Create central widget and main layout
        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")  # For stylesheet targeting
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(25)  # Spacing between widgets
        main_layout.setContentsMargins(30, 30, 30, 30)  # Margins around the layout

        # Add title bar (custom, since we have no frame)
        self.create_title_bar(main_layout)

        # Create battery info instance *here*
        self.battery_info = BatteryInfo()

        # Create UI elements (sections)
        self.create_percentage_section(main_layout)
        self.create_status_section(main_layout)
        self.create_details_section(main_layout)

        # Add refresh button (using the resource system)
        refresh_button = QPushButton(" Refresh")
        refresh_button.setIcon(QIcon(":/icons/refresh_icon.png"))  # Load from resource file
        refresh_button.setMinimumHeight(45)
        refresh_button.clicked.connect(self.update_battery_info)
        main_layout.addWidget(refresh_button)

        main_layout.addStretch()  # Push everything to the top

        # Set up auto-refresh timer (every 30 seconds)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_battery_info)
        self.timer.start(30000)  # 30 seconds in milliseconds

        # Initial update
        self.update_battery_info()
        self.dragPos = None

    def create_title_bar(self, parent_layout):
        """Creates a custom title bar with a close button."""
        title_bar = QHBoxLayout()

        title_label = QLabel("Battery Monitor")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))

        close_button = QPushButton("×")
        close_button.setFixedSize(30, 30)  # Square button
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #ff4444; /* Red */
                border-radius: 15px; /* Circular */
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff6666; /* Lighter Red on hover */
            }
        """)
        close_button.clicked.connect(self.close)  # Connect to close()

        title_bar.addWidget(title_label)
        title_bar.addStretch()  # Push close button to the right
        title_bar.addWidget(close_button)

        parent_layout.addLayout(title_bar)  # Add to the parent layout


    def create_percentage_section(self, parent_layout):
        """Creates the battery percentage section."""
        percentage_frame = CustomFrame()  # Use the custom frame
        percentage_layout = QVBoxLayout(percentage_frame)
        percentage_layout.setContentsMargins(25, 25, 25, 25)

        self.progress_bar = AnimatedProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setMinimumHeight(35)
        self.progress_bar.setTextVisible(False) # Hide the default percentage text
        percentage_layout.addWidget(self.progress_bar)

        self.percentage_label = QLabel("---%")  # Initial placeholder
        self.percentage_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.percentage_label.setFont(QFont("Arial", 56, QFont.Weight.Bold))  # Large font
        self.percentage_label.setStyleSheet("color: #ffffff;")  # White text
        percentage_layout.addWidget(self.percentage_label)

        parent_layout.addWidget(percentage_frame)


    def create_status_section(self, parent_layout):
        """Creates the battery status section."""
        status_frame = CustomFrame()
        status_layout = QVBoxLayout(status_frame)
        status_layout.setContentsMargins(25, 25, 25, 25)

        self.status_label = QLabel("Status: Unknown")
        self.status_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.time_remaining_label = QLabel("Time Remaining: N/A")
        self.time_remaining_label.setFont(QFont("Arial", 14))

        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.time_remaining_label)

        parent_layout.addWidget(status_frame)

    def create_details_section(self, parent_layout):
        """Creates the battery details section."""
        details_frame = CustomFrame()
        details_layout = QVBoxLayout(details_frame)
        details_layout.setContentsMargins(25, 25, 25, 25)

        self.health_label = QLabel("Battery Health: N/A")  # Placeholder
        self.health_label.setFont(QFont("Arial", 14))
        self.plugged_label = QLabel("Power Supply: N/A")
        self.plugged_label.setFont(QFont("Arial", 14))

        details_layout.addWidget(self.health_label)
        details_layout.addWidget(self.plugged_label)

        parent_layout.addWidget(details_frame)

    def mousePressEvent(self, event):
        """Handles mouse press events for window dragging."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Handles mouse move events for window dragging."""
        if event.buttons() == Qt.MouseButton.LeftButton and self.dragPos:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()

    def update_battery_info(self):
        """Updates the UI with the latest battery information."""
        try:
            info = self.battery_info.get_battery_info()

            percentage = info['percentage']
            self.percentage_label.setText(f"{percentage}%")
            self.progress_bar.setValue(percentage)

            # Dynamic color based on percentage
            if percentage <= 20:
                color = "#ff4444"  # Red
                self.percentage_label.setStyleSheet("color: #ff4444;")
            elif percentage <= 50:
                color = "#ffaa00"  # Orange
                self.percentage_label.setStyleSheet("color: #ffaa00;")
            else:
                color = "#00cc44"  # Green
                self.percentage_label.setStyleSheet("color: #00cc44;")

            self.progress_bar.setStyleSheet(f"""
                QProgressBar::chunk {{
                    background-color: {color};
                    border-radius: 6px;
                }}
            """)

            # Update status with dynamic styling
            status = info['status']
            status_color = "#00cc44" if status == "Fully Charged" else "#ffffff"
            self.status_label.setStyleSheet(f"color: {status_color};")
            self.status_label.setText(f"Status: {status}")

            self.time_remaining_label.setText(
                f"Time Remaining: {info['time_remaining']}")

            power_status = 'Plugged In' if info['is_plugged'] else 'Battery'
            self.plugged_label.setText(f"Power Supply: {power_status}")

            #  We keep this for consistency, even if we don't have a reliable way
            #  to get the actual battery health on all systems.
            self.health_label.setText("Battery Health: N/A")

        except Exception as e:
            self.show_error_state(str(e))

    def show_error_state(self, error_message):
        """Displays an error state in the UI."""
        self.percentage_label.setText("N/A")
        self.percentage_label.setStyleSheet("color: #ff4444;")  # Red
        self.progress_bar.setValue(0)  # Reset progress bar
        self.status_label.setText("Status: Error")
        self.status_label.setStyleSheet("color: #ff4444;")  # Red
        self.time_remaining_label.setText("Time Remaining: N/A")
        self.health_label.setText("Battery Health: N/A")
        self.plugged_label.setText("Power Supply: Unknown")