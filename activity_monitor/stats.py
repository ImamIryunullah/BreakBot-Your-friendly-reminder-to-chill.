import json
import os
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

LOG_FILE = os.path.join(os.path.dirname(__file__), "data", "activity_log.json")

def load_activity_data(filepath='activity_log.don'):
    with open(filepath, 'r') as f:
        content = f.read().strip()
        if not content:
            print("File log nya masih kosongg")
            return []
        return json.load(content)

def plot_daily_activity():
    if not os.path.exists(LOG_FILE):
        print("Log file belum ada.")
        return

    with open(LOG_FILE, 'r') as f:
        data = json.load(f)

    hours = [datetime.fromisoformat(ts).hour for ts in data]

    count_by_hour = Counter(hours)

    hours_list = list(range(24))
    counts = [count_by_hour.get(h, 0) for h in hours_list]

    plt.bar(hours_list, counts)
    plt.xlabel("Jam")
    plt.ylabel("Jumlah aktivitas")
    plt.title("Statistik Aktivitas Harian")
    plt.xticks(hours_list)
    plt.show()
