# HtmlParser.py
from bs4 import BeautifulSoup
import mesage

class HtmlParser:
    def __init__(self, html, ogrenciNo):
        self.get_page = html
        self.result = []
        self.ogrenciNo = ogrenciNo
        self.result.append(self.ogrenciNo)
        self.parser(self.get_page)

    def parser(self, html_content):
        if not html_content:
            print("Hata: HTML içeriği alınamadı!")
            return

        soup = BeautifulSoup(html_content, "html.parser")
        divs = soup.find("div", {"class": "table-responsive"})
        
        if not divs:
            print("Hata: Tablo bulunamadı!")
            return

        dersler = divs.find_all("tr")
        for ders in dersler:
            sutunlar = ders.find_all("td")
            if not sutunlar:
                continue

            if sutunlar[0].get("rowspan") == "2":
                ders_adi = sutunlar[1].text.strip()
                sinav_bilgileri = []

            if sutunlar[0].get("colspan") == "4":
                for td in sutunlar:
                    alt_tablo = td.find("table")
                    if alt_tablo:
                        for tr in alt_tablo.find_all("tr"):
                            sinav = tr.find_all("td")
                            if len(sinav) >= 2:
                                sinav_bilgileri.append(f"{sinav[0].text.strip()}: {sinav[1].text.strip()}")

                self.result.append(f"{ders_adi}  -->  {' | '.join(sinav_bilgileri) if sinav_bilgileri else 'Sınav bilgisi yok'}")
        
        self.result2 = "\n".join(self.result)

        mesage.send_message("your bot token", "chat id", self.result2)
