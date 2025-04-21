UBYS Botu
Python ile geliştirilen bu bot, OMÜ'nün UBYS sistemine otomatik giriş yapar ve çeşitli kullanıcı işlemlerini yönetmek için temel bir altyapı sunar.

Özellikler
UBYS sistemine otomatik giriş

HTML içeriklerden veri çekme

Kullanıcı yönetimi

Otomatik oturum başlatma ve kontrol

Giriş hatalarını loglama

Dosya Yapısı
login.py: UBYS giriş işlemleri ve token alma işlemleri burada gerçekleşir.

manager.py: Giriş yapan kullanıcıların oturum yönetimi.

main.py: Uygulamanın giriş noktası.

mesage.py, mesage_control.py: Mesaj işlemleriyle ilgilenir.

parser.py: UBYS'den gelen HTML yanıtlarını parse eder.

users.py: Kullanıcı bilgileri (örnek kullanıcı listesi).

Kurulum
Gerekli kütüphaneleri yükleyin:

nginx
Kopyala
Düzenle
pip install requests beautifulsoup4
users.py dosyasını düzenleyerek kendi kullanıcı bilgilerinizi girin.

Uygulamayı başlatın:

css
Kopyala
Düzenle
python main.py
Uyarı
Bu proje eğitim amaçlı geliştirilmiştir.

Şahsi bilgilerinizi kimseyle paylaşmayınız.

UBYS sistemine aşırı istek göndermek sisteme zarar verebilir; sorumluluk kullanıcıya aittir.

Geliştirici Notu
Kod sade ve modüler olacak şekilde yazılmıştır. Yeni özellikler eklemek için manager.py üzerinden ilerleyebilirsiniz.
