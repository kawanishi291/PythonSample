import datetime
import csv
import pandas as pd

def InputData():
    val = int(input())

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
    print(csv_input.size)
    #返却される型は、numpy.ndarray
    print(csv_input.values)