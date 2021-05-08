from def01 import *

month = int(input("月 >> "))
day = int(input("日 >> "))
f_month, f_day = calc(day + 25, month-1)
e_month, e_day = calc(day + 38, month-1)
print(str(f_month) + "月" + str(f_day) + "日〜" + str(e_month) + "月" + str(e_day) + "日")