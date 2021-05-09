import requests
from bs4 import BeautifulSoup
import re
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


def InputData(msg):
    val = input(msg)

    return val


def ScrapingGitHub(url):
    site = requests.get(url)
    data = BeautifulSoup(site.text, "html.parser")
    data_list = data.find_all("rect") #すべての「a」タグを出力する

    return data_list


def MakeTxtInputList(data_list, file_name):
    with open(file_name, 'w') as f:
        for val in data_list:
            f.write(str(val) + "\n")

    with open(file_name, 'r') as f:
        s = f.read()
        data_list = re.findall('data-count=.* d', s)
        
    commit_list = []
    date_list = []
    for items in data_list:
        item = items[:-3]
        num_list = re.findall('[0-9]', item)
        if len(num_list) == 9:
            commit_list.append(int(num_list[0]))
            date_list.append(num_list[1:][0] + num_list[1:][1] + num_list[1:][2] + num_list[1:][3] + "-" + num_list[1:][4] + num_list[1:][5] + "-" + num_list[1:][6] + num_list[1:][7])
        else:
            sum_cnt = 0
            for i in range(0, len(num_list)-8):
                sum_cnt *= 10
                sum_cnt += int(num_list[:len(num_list)-8][i])
            commit_list.append(sum_cnt)
            date_list.append(num_list[len(num_list)-8:][0] + num_list[len(num_list)-8:][1] + num_list[len(num_list)-8:][2] + num_list[len(num_list)-8:][3] + "-" + num_list[len(num_list)-8:][4] + num_list[len(num_list)-8:][5] + "-" + num_list[len(num_list)-8:][6] + num_list[len(num_list)-8:][7])

    return commit_list, date_list


def CheckFile(filename):
    if os.path.exists(filename) == False:
        word = "日,コミット数"
        words = word.split(',')
        with open(filename, 'w') as f :
            writer = csv.writer(f)
            writer.writerow(words)


def WrightCSV(filename, commit_list, date_list):
    for i in range(0, len(commit_list)):
        word = date_list[i] + ',' + str(commit_list[i])
        words = word.split(',')
        with open(filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(words)



def PrintGraph(filename):
    csv_input = pd.read_csv(filepath_or_buffer = filename, encoding = "utf_8", sep = ",")
    cnt = int(csv_input.size.item()/2) # 730(行 * 列)
    commit = []
    for i in range(0, cnt):
        commit.append(csv_input.values[i][1])
    data = np.array(commit)
    date = np.array(range(1, cnt+1))
    plt.plot(date, data)
    plt.xlim([1, len(commit)])
    plt.ylim([0, 50])
    plt.show()