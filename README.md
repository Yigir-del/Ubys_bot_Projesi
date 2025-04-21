# UBYS Automation Bot 🚀

UBYS (Ondokuz Mayıs Üniversitesi Bilgi Yönetim Sistemi) için geliştirilmiş, terminal tabanlı bir otomasyon betiği.

## Özellikler

- UBYS sistemine programatik olarak login olur.
- Oturum yönetimi yapar, geçerli sessionları kontrol eder.
- HTML response'ları `BeautifulSoup` ile parse eder.
- Kullanıcıya ait bilgileri çeker, doğrular, işler.

## Modüller

- `main.py` → Botun çalıştığı ana script. Giriş noktasıdır.
- `login.py` → Login işlemleri. UBYS token’ını alır.
- `manager.py` → Kullanıcıları tanımlar, oturumları kontrol eder.
- `parser.py` → UBYS'den gelen HTML'i parse eder.
- `message.py` → Bot içi mesaj formatları burada tanımlı.
- `mesage_control.py` → Mesaj kontrol fonksiyonları.
- `users.py` → Kullanıcı listesi. Örnek veri barındırır.

## Kullanım

```bash
git clone https://github.com/kullaniciadi/ubys_bot.git
cd ubys_bot
pip install -r requirements.txt
python main.py

Gereksinimler
Python 3.x
requests
beautifulsoup4

Uyarılar
users.py içinde örnek kullanıcılar var. Gerçek UBYS bilgilerini sen girmelisin.
Bu araç tamamen eğitim amaçlıdır. UBYS sistemine yapılacak aşırı isteklerden geliştirici sorumlu değildir.
Sistemde tutulan hiçbir veri dışa aktarılmaz, güvenliğe özen gösterilmiştir.
