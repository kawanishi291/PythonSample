import os
from def05 import *

msg = "あなたのGitHubのURLを入力してください >> "
url = InputData(msg)
# スクレイピングしコミット数に関連する部分をリスト化
data_list = ScrapingGitHub(url)

file_name = "sample.txt"
# リスト化したデータでファイルを生成し、コミット数・日付のそれぞれをリスト化
commit_list, date_list = MakeTxtInputList(data_list, file_name)
# 不要なファイルを破棄
os.remove(file_name)

file_name = date_list[len(date_list)-1] + ".csv"
# csvファイルを生成
CheckFile(file_name)
# データをcsvファイルに書き込み
WrightCSV(file_name, commit_list, date_list)

# csvを読み込みグラフを作成
PrintGraph(file_name)
# 不要なファイルを破棄
os.remove(file_name)
