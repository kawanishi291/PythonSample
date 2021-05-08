import datetime
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def InputData(msg):
    val = int(input(msg))

    return val


def WrightFile(data):
    dt_now = datetime.datetime.now()
    file_name = "check_" + str(dt_now.year) + ".txt"
    with open(file_name, 'w') as f:
        f.write(str(data) + "円\n")


def WrightCSV(data):
    dt_now = datetime.datetime.now()
    file_name = "check_" + str(dt_now.year) + ".csv"
    word = str(dt_now.month) + "月," + str(data)
    words = word.split(',')
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(words)


def ReadCSV():
    dt_now = datetime.datetime.now()
    file_name = "check_" + str(dt_now.year) + ".csv"
    csv_input = pd.read_csv(filepath_or_buffer = file_name, encoding = "utf_8", sep = ",")
    # インプットの項目数（行数 * カラム数）を返却します。
    #print(csv_input.size)
    #返却される型は、numpy.ndarray
    #print(csv_input.values)

    return csv_input.values


def checkMonth(csv_list):
    length = len(csv_list)
    this_month = csv_list[length-1][0]
    dt_now = datetime.datetime.now()
    if str(dt_now.month) + "月" == this_month:
        return 1
    else:
        return 0


def SortingData(csv_values):
    month = []
    data = []
    for key, val in csv_values:
        m = key.replace('月', '')
        month.append(int(m))
        data.append(val)
    
    return month, data


def DrawingGraph(month, data):
    
    month = np.array(month)
    data = np.array(data)
    plt.plot(month, data)
    plt.xlim([1, 13])
    plt.ylim([0, 2000])
    plt.show()