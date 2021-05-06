import os
import glob

from smb.SMBConnection import SMBConnection
path = os.getcwd() #現在の作業フォルダ位置を取得
sendFileFolder = os.path.join(path, "送信データ")
reciveFileFolder = os.path.join(path, "受信データ")
user = "" # サーバ接続ユーザ名
password = "" # サーバ接続パスワード
ipAdress = "192.168.130.100" #サーバIPアドレス
serverFolder = "test"
connection = SMBConnection(user, password, "myClient", "HostServer")

os.chdir(sendFileFolder)
for sendFile in glob.glob("*.xlsx"):
    with open(sendFile, "rb") as file:
        connection.storeFile(serverFolder, sendFile, file)
os.chdir(reciveFileFolder)
for reciveFile in connection.listPath (serverFolder, '/'):
    if reciveFile.filename == "..":
        continue
    with open(reciveFile.filename, 'wb') as file:
        connection.retrieveFile (serverFolder, reciveFile.filename, file)
connection.close()
