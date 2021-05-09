import requests
from bs4 import BeautifulSoup

site = requests.get("https://www.google.com")
requests.get("https://www.google.com")
data = BeautifulSoup(site.text, "html.parser")
print(data.title) #タイトルを出力する
print(data.title.text) #タイトルタグの中身のみを出力する
print(data.find_all("a")) #すべての「a」タグを出力する
print(data.find(id="id_name")) #id属性「id_name」に一致するタグを出力する
print(data.find(text="Google")) #特定のワード「Google」に完全一致する文字列を出力する