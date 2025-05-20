from activity_monitor.monitor import ActivityMonitor
from activity_monitor.gui import get_user_setting
from activity_monitor.stats import plot_daily_activity
import sys

def main():
    user_seconds = get_user_setting()
    monitor = ActivityMonitor(max_active_time=user_seconds)
    monitor.run()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "stats":
        plot_daily_activity()
    else:
        main()