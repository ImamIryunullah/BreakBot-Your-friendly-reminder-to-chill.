from plyer import notification
from playsound import playsound
import threading

def notify_user(title="Istirahat Dulu Gak Sih Ngabsss!!!", message="Sudah lama kamu aktif, waktunya istirahat doeloe sihhhh !"):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )
    threading.Thread(target=playsound, args=("alert.mp3",), daemon=True).start()
