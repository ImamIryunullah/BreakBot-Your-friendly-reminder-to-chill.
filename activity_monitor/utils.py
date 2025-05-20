import json, os
from datetime import datetime
from plyer import notification
from playsound import playsound 

LOG_FILE = "activity_log.json"
SOUND_FILE = os.path.join(os.path.dirname(__file__), "alert.mp3")

def log_activity():
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    data = load_log()
    data.append({"timestamp": time_str})
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_log():
    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        return []
    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

def play_alarm():
    try:
        playsound(SOUND_FILE)
    except Exception as e:
        print("Gagal memutar suara:", e)
