from defainHealth import *

year = inputNumber("西暦 => ", 1900, 9999)
month = inputNumber("月 => ", 1, 12)
day = inputNumber("日 => ", 1, LastDayOfTheMonth(year, month))

f_month, f_day = calc(year, month-1, day + 25)
e_month, e_day = calc(year, month-1, day + 38)

print("正常 >> " + str(f_month) + "月" + str(f_day) + "日〜" + str(e_month) + "月" + str(e_day) + "日")

if e_month == f_month:
    flag = 1
else:
    flag = 2

for i in range(0, flag):
    cnt = countLeapYear(year)
    days = countAllDays(year, f_month + i, cnt)
    blank = (days + 1) % 7
    printCalendar(year, f_month + i, blank)