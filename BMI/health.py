from defHealth import *

while True:
    val = InputData("0:追加, 1:閲覧 => ")
    if val == 0:
        print("追加")
        csv_values = ReadCSV()
        flag = checkMonth(csv_values)
        if flag == 0:
            data = InputData("金額 >> ")
            WrightCSV(data)
        else:
            print("今月の入力は終了しました")
        break
    elif val == 1:
        print("閲覧")
        csv_values = ReadCSV()
        month, data = SortingData(csv_values)
        DrawingGraph(month, data)
        break
    else:
        print("error")
        print("0 か 1 で入力してください")
