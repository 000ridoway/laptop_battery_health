# src/battery_monitor/widgets.py

from PySide6.QtWidgets import (QFrame, QProgressBar, QGraphicsDropShadowEffect) # Changed from PyQt6
from PySide6.QtCore import QPropertyAnimation, QEasingCurve # Changed from PyQt6
from PySide6.QtGui import QColor # Changed from PyQt6


class CustomFrame(QFrame):
    """A custom QFrame with rounded corners, a border, and a shadow."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)

        # Add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 80))  # Semi-transparent black
        shadow.setOffset(0, 2)  # Slight downward offset
        self.setGraphicsEffect(shadow)

        self.setStyleSheet("""
            CustomFrame {
                background-color: #2d2d2d; /* Dark gray */
                border-radius: 15px; /* Rounded corners */
                border: 1px solid #3d3d3d; /* Slightly lighter border */
                padding: 10px; /* Add some padding inside the frame */
            }
        """)


class AnimatedProgressBar(QProgressBar):
    """A QProgressBar with smooth value transitions."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QPropertyAnimation(self, b"value")
        self._animation.setEasingCurve(QEasingCurve.Type.OutCubic)  # Smooth easing
        self._animation.setDuration(1000)  # 1 second animation

    def setValue(self, value):
        """Sets the value with animation."""
        self._animation.stop()  # Stop any previous animation
        self._animation.setStartValue(self.value())  # Start from current value
        self._animation.setEndValue(value)  # Animate to the new value
        self._animation.start()