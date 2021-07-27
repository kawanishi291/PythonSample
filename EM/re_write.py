import ast
import json

def ReadText(path):
    with open(path) as f:
        data = f.read()

    return data

def SetData(path):
    data = ReadText(path)
    dict = ast.literal_eval(data)
    key_list = dict.keys()

    return dict, key_list

def ChangeValue(num):
    for t in range(1, 20):
        if (350 * t) <= num and num <= (500 * t):
            num = t * 425
            return num

    return (num // 350) * 425

def WriteText(path, text):
    with open(path, mode='w') as f:
        f.write(text)


def main():
    path = './codes'
    dict, key_list = SetData(path)
    for title in key_list:
        for i in range(len(dict[title])):
            num = dict[title][i]
            num = ChangeValue(num)
            dict[title][i] = num
    text = json.dumps(dict)
    #print(text)
    WriteText(path, text)


if __name__ == "__main__":
    main()