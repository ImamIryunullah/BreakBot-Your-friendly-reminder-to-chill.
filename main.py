import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from activity_monitor.monitor import ActivityMonitor
from activity_monitor.config import MAX_ACTIVE_TIME

def main():
    monitor = ActivityMonitor(max_active_time=MAX_ACTIVE_TIME)
    monitor.run()

if __name__ == "__main__":
    main()
