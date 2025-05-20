from activity_monitor.monitor import ActivityMonitor
from activity_monitor.gui import get_user_setting

def main():
    user_seconds = get_user_setting()
    monitor = ActivityMonitor(max_active_time=user_seconds)
    monitor.run()

if __name__ == "__main__":
    main()
