from .def06 import *

# TOPページ表示関数
# ScrapingTsudanumaInfo("http://localhost/html/index.html")

# セッションを開始
session = requests.session()
# メールアドレスとパスワードの指定
USER = "sneky56347.sk@gmail.com"
PASS = "0000"
# ログイン関数
TsudanumaInfoLogin(USER, PASS)
TsudanumaInfoMypage(session, "http://localhost/template/user.php")
