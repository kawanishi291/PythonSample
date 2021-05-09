import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def ScrapingTsudanumaInfo(url):
    site = requests.get(url)
    data = BeautifulSoup(site.content, "html.parser")
    print(data.text)


def TsudanumaInfoLogin(USER, PASS):
    # セッションを開始
    session = requests.session()
    # ログイン
    login_info = {
        "email":USER,
        "pass":PASS
    }
    # action
    url_login = "http://localhost/account/login-check.php"
    res = session.post(url_login, data=login_info)
    res.raise_for_status() # エラーならここで例外を発生させる
    print(res.text)


def TsudanumaInfoMypage(session, url_mypage):
    res = session.get(url_mypage)
    res.raise_for_status()
    print(res.text)