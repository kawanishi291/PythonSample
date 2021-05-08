from defHealth import *

print("健康管理")
while True:
    val = InputData("0:追加, 1:閲覧 => ")
    if val == 0:
        print("追加")
        csv_values = ReadCSV()
        flag = checkDay(csv_values)
        if flag == 0:
            data = InputData("体重(kg) >> ")
            WrightCSV(data)
        else:
            print("今日の入力は終了しました")
        break
    elif val == 1:
        print("閲覧")
        csv_values = ReadCSV()
        day, data = SortingData(csv_values)
        min_weight, max_weight = MinMaxWeight(data)
        DrawingGraph(day, data, min_weight, max_weight)
        break
    else:
        print("error")
        print("0 か 1 で入力してください")
