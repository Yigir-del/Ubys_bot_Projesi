# mesage_control.py

import os

def set_active(status: bool):
    """Botun aktif durumu dosyada güncellenir."""
    try:
        with open("status.txt", "w") as f:
            f.write("1" if status else "0")
    except Exception as e:
        print(f"status.txt dosyasına yazma hatası: {e}")

def is_active() -> bool:
    """Aktiflik durumunu kontrol et. Dosyadaki değeri okur."""
    try:
        # Dosyanın varlığını kontrol et
        if not os.path.exists("status.txt"):
            return False
        
        with open("status.txt", "r") as f:
            status = f.read().strip()
            return status == "1"
    except Exception as e:
        print(f"status.txt dosyasını okuma hatası: {e}")
        return False
