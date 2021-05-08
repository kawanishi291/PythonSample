import requests
import datetime
import pandas as pd
import pyperclip
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def pasteUrl(e):
    urlText.delete("1.0", "end")
    urlText.insert("1.0", pyperclip.paste())

def getData():
    url = urlText.get("1.0", "end")
    html_contents = requests.get(url).text
    html_soup = BeautifulSoup(html_contents, "html.parser")
    prices = html_soup.find_all("span", {"class": "a-color-parser"})
    price = None
    for p in prices:
        if "¥" in p.text:
            price = p.text
            break
    item_name = html_soup.find("", {"id": "productTitle"}).text
    item_name = item_name.replace("\n", "")
    df = pd.read_excel("Amazon.xlsx")
    data = [datetime.datetime.now(), item_name, price, url]
    df2 = pd.DataFrame([data], columns = df.columns)
    df = df.append(df2)
    with pd.ExcelWriter("Amazon.xlsx") as writer:
        df.to_excel(writer, index = False, columns = df.columns)
    messagebox.showinfo("完了", "エクセルデータの書き出しが完了しました。")


root = tk.Tk()
root.title("商品データ書き出し")
root.geometry("700x55")
root.grid()
urlLabel = tk.Label(root, text = "URL")
urlText = tk.Text(root, borderwidth = 3, height = 3, relief = "ridge")
urlText.bind("<Button-1>", pasteUrl)
getButton = tk.Button(root, text = "データ取得", command = getData)
urlLabel.grid(row = 1, column = 1)
urlText.grid(row = 1, column = 2)