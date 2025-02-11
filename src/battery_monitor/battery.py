# src/battery_monitor/battery.py
import psutil
from datetime import timedelta

class BatteryInfo:
    def __init__(self):
        self.battery = None
        self.has_battery = True
        self._initialize_battery()

    def _initialize_battery(self):
        try:
            self.battery = psutil.sensors_battery()
            if self.battery is None:
                self.has_battery = False
        except Exception as e:
            #  Handle cases where psutil might not be supported
            #  or sensors_battery() raises an exception.
            print(f"Error initializing battery: {e}")
            self.has_battery = False

    def get_battery_info(self):
        try:
            self._initialize_battery()  # Refresh battery info

            if not self.has_battery:
                return {
                    'percentage': 100,  # Default to 100% if no battery
                    'is_plugged': True,  # Assume plugged in if no battery
                    'status': "No Battery (PC)",
                    'time_remaining': "N/A"
                }

            info = {
                'percentage': int(self.battery.percent),
                'is_plugged': self.battery.power_plugged,
                'status': self._get_status(),
                'time_remaining': self._format_time_remaining()
            }

            # Add battery health if available
            # Note: This is platform-dependent and might not be available
            # You might need to use additional Windows-specific APIs for this
            #  We'll leave it as N/A for now, for maximum compatibility.

            return info

        except Exception as e:
            raise RuntimeError(f"Failed to get battery information: {str(e)}")

    def _get_status(self):
        if not self.has_battery:
            return "No Battery (PC)"
        if self.battery.power_plugged:
            if self.battery.percent >= 100:
                return "Fully Charged"
            return "Charging"
        return "Discharging"

    def _format_time_remaining(self):
        if not self.has_battery:
            return "N/A"
        if self.battery.secsleft == psutil.POWER_TIME_UNLIMITED:
            return "Unlimited"  # Plugged in and full
        elif self.battery.secsleft == psutil.POWER_TIME_UNKNOWN:
            return "Calculating..."  # Can't determine time
        elif self.battery is None:  # Handle case of no battery object.
             return "N/A"

        # Convert seconds to hours and minutes
        time = timedelta(seconds=self.battery.secsleft)
        hours = time.seconds // 3600
        minutes = (time.seconds % 3600) // 60

        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"