import time
from datetime import datetime
import mesage_control
import users
import login
import requests

class Manager:
    def __init__(self, name, password, sapid):
        self.name = name
        self.password = password
        self.sapid = sapid
        self.omu = login.OMULogin(self.name, self.password)

    def start(self):
        try:
            session = self.omu.login()
            if isinstance(session, requests.Session):
                print(f"[{datetime.now()}] {self.name}: Oturum açıldı.")
                self.omu.get_page_content(self.sapid)
            else:
                print(f"[{datetime.now()}] {self.name}: Giriş Hatası - {session}")
        except Exception as e:
            print(f"[{datetime.now()}] {self.name}: Hata - {str(e)}")

def run_manager_loop():
    print("Manager başlatıldı.")
    start_time = time.time()
    while True:
        if not mesage_control.is_active():
            print("[manager] Bot durdu. Bekliyor...")
            time.sleep(5)  # Durduysa bekle ve tekrar kontrol et
            continue  # Eğer bot durursa, döngü tekrar başa dönsün

        for user in users.user_list:
            try:
                manager = Manager(user["name"], user["password"], user["sapid"])
                manager.start()
                time.sleep(600)
            except Exception as e:
                print(f"{user['name']} hata: {str(e)}")

        # 30 dakika sonra yeniden işlem başlat
        if time.time() - start_time >= 1800:
            print("[manager] 30 dakika doldu, döngü sıfırlanıyor...")
            start_time = time.time()
        else:
            time.sleep(10)
