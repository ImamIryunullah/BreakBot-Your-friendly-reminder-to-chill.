import os
import json
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
LOG_FILE = os.path.join(DATA_DIR, "activity_log.json")

os.makedirs(DATA_DIR, exist_ok=True)

def log_activity():
    now = datetime.now().isoformat()
    data = load_log()
    data.append(now)
    with open(LOG_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        return json.load(f)
