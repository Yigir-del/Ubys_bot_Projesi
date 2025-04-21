import requests
from bs4 import BeautifulSoup
import parser

class OMULogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()

    def get_login_token(self):
        """Giriş sayfasından CSRF tokenini alır."""
        login_page_url = "https://ubys.omu.edu.tr/"
        response = self.session.get(login_page_url)

        if response.status_code != 200:
            print(f"Hata: Giriş sayfası yüklenemedi! Kod: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        token_input = soup.find("input", {"name": "__RequestVerificationToken"})
        if token_input:
            return token_input["value"]
        
        print("Hata: Token bulunamadı!")
        return None

    def login(self):
        """Login işlemi yapılır."""
        csrf_token = self.get_login_token()
        if not csrf_token:
            print("Token alınamadı. Giriş başarısız!")
            return None

        payload = {
            "username": self.username,
            "password": self.password,
            "__RequestVerificationToken": csrf_token,
            "xmlhttp": "XMLHttpRequest",
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = self.session.post("https://ubys.omu.edu.tr/Account/Login", data=payload, headers=headers)
        if response.status_code == 200:
            print("Login Başarılı.")
            return self.session

        print(f"Giriş başarısız! Kod: {response.status_code}")
        print("Hata içeriği:", response.text)
        return response

    def get_page_content(self, page_url):
        """Belirtilen sayfanın HTML içeriğini alır."""
        response = self.session.get(page_url)
        if response.status_code != 200:
            print(f"HTML alınamadı! Kod: {response.status_code}")
            print("Hata içeriği:", response.text)
            return

        html_content = response.text
        if html_content:
            parser.HtmlParser(html_content,self.username)
        else:
            print("Hata: HTML içeriği boş!")
