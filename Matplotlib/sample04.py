from define04 import InputData, WrightFile, WrightCSV, ReadCSV

while True:
    print("0:追加, 1:閲覧")
    val = InputData()
    print(val)
    if val == 0:
        print("追加")
        data = InputData()
        WrightCSV(data)
        break
    elif val == 1:
        print("閲覧")
        ReadCSV()
        break
    else:
        print("error")
        print("0 か 1 で入力してください")
