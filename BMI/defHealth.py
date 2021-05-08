import os
import datetime
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def InputData(msg):
    val = int(input(msg))

    return val


# def WrightFile(data):
#     dt_now = datetime.datetime.now()
#     file_name = "health_" + str(dt_now.year) + "_" + str(dt_now.month) + ".txt"
#     with open(file_name, 'w') as f:
#         f.write(str(data) + "円\n")


def WrightCSV(data):
    dt_now = datetime.datetime.now()
    file_name = "health_" + str(dt_now.year) + "_" + str(dt_now.month) + ".csv"
    word = str(dt_now.day) + "日," + str(data)
    words = word.split(',')
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(words)


def ReadCSV():
    dt_now = datetime.datetime.now()
    file_name = "health_" + str(dt_now.year) + "_" + str(dt_now.month) + ".csv"
    checkFile(file_name)
    csv_input = pd.read_csv(filepath_or_buffer = file_name, encoding = "utf_8", sep = ",")
    # インプットの項目数（行数 * カラム数）を返却します。
    # print(csv_input.size)
    # 返却される型は、numpy.ndarray
    # print(csv_input.values)

    return csv_input.values


def checkDay(csv_list):
    length = len(csv_list)
    if length > 0:
        this_day = csv_list[length-1][0]
        dt_now = datetime.datetime.now()
        if str(dt_now.day) + "日" == this_day:
            flag = 1
        else:
            flag = 0
    else:
        flag = 0
    
    return flag


def SortingData(csv_values):
    day = []
    data = []
    for key, val in csv_values:
        m = key.replace('日', '')
        day.append(int(m))
        data.append(val)
    
    return day, data


def DrawingGraph(day, data):
    
    day = np.array(day)
    data = np.array(data)
    plt.plot(day, data)
    plt.xlim([1, 31])
    plt.ylim([20, 100])
    plt.show()


def checkFile(filename):
    if os.path.exists(filename) == False:
        word = "日,体重"
        words = word.split(',')
        with open(filename, 'w') as f :
            writer = csv.writer(f)
            writer.writerow(words)