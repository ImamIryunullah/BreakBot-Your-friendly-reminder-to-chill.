import time
from threading import Timer
from activity_monitor.utils import log_activity
from pynput import keyboard, mouse
from activity_monitor.notifier import notify_break

class ActivityMonitor:
    def __init__(self, max_active_time):
        self.max_active_time = max_active_time
        self.timer = None

    def start_timer(self):
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(self.max_active_time, self.handle_break)
        self.timer.start()

    def handle_break(self):
        notify_break()
        self.start_timer()      

    def on_activity(self, event):
        log_activity()
        self.start_timer()

    def run(self):
        self.start_timer()

        def on_press(key):
            self.on_activity(key)

        def on_move(x, y):
            self.on_activity(None)

        def on_click(x, y, button, pressed):
            self.on_activity(None)

        def on_scroll(x, y, dx, dy):
            self.on_activity(None)

        with keyboard.Listener(on_press=on_press) as kl, \
             mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as ml:
            print("Monitoring aktivitas keyboard dan mouse... Tekan Ctrl+C untuk keluar.")
            kl.join()
            ml.join()
