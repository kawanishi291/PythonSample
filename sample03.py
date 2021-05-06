# Google Drive からファイルを取得
from urllib.parse import urlparse
import urllib.request
import requests

url = "https://drive.google.com/drive/folders/1lIea-72WzDJHc1gLlf0OJhWqm8kUbHMQ?usp=sharing"
workUrl = "https://docs.google.com/uc?id=<file_id>"
path = urlparse(url).path
path = path.lstrip("/file/d")
path = path.rstrip("/view")
url = workUrl.replace("<file_id>", path)
response = requests.get(url)
file_name = "sample01.html"
with open(file_name, 'wb') as sf:
    sf.write(response.content)