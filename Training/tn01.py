# 2つの正の整数値を入力させ、互いに素であるか判定するプログラムを作成せよ。
# なお、2つの正の整数が互いに素とは、1以外に共通公約数を持たない関係のことである。

def PrimeNumber(num):
    cnt = 0
    flag = 0

    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt <= 2:
        flag = 1
    
    return flag



num1, num2 = input("2つの値をスペースで区切って入力: ").split()
# print(int(num1) + 1, int(num2) - 1)
num1 = int(num1)
num2 = int(num2)
flag1 = PrimeNumber(num1)
flag2 = PrimeNumber(num2)
if flag1 == 1 and flag2 == 1:
    print("互いに素")
else:
    print("互いに素でない")
