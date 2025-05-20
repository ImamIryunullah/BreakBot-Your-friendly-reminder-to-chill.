from pynput import mouse, keyboard
import time
from .utils import log_activity, send_notification, play_alarm

class ActivityMonitor:
    def __init__(self, max_active_time=3600):
        self.max_active_time = max_active_time
        self.last_active_time = time.time()
        self.active = True

    def on_activity(self, key=None):
        self.last_active_time = time.time()
        log_activity()

    def on_move(self, x, y):
        self.on_activity()

    def run(self):
        print("Monitoring aktivitas keyboard dan mouse... Tekan Ctrl+C untuk keluar.")
        with mouse.Listener(on_move=self.on_move) as ml, \
             keyboard.Listener(on_press=self.on_activity) as kl:
            try:
                while True:
                    time.sleep(1)
                    now = time.time()
                    if now - self.last_active_time > self.max_active_time:
                        send_notification("Istirahat dulu!", "Kamu sudah aktif terlalu lama")
                        play_alarm()
                        self.last_active_time = now  # reset
            except KeyboardInterrupt:
                print("Monitoring dihentikan.")
