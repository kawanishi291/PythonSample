month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 閏年カウント
def countLeapYear(year):
    cnt = 0
    for i in range(1900, year):
        cnt += checkLeapYear(i)

    return cnt


def checkLeapYear(num):
    if ((num % 4 == 0) and (num % 100 != 0)) or (num % 400 == 0):
        return 1
    else:
        return 0


def countAllDays(year, month, cnt):
    days = (year - 1900) * 365 + cnt
    for i in range(0, month-1):
        days += month_list[i]
    
    return days


# カレンダー表示
def printCalendar(y, m, blank):
    flag = checkLeapYear(y)
    print(" --------------------")
    print(" 日 月 火 水 木 金 土")
    for i in range(0, blank):
        print("   ", end="")
    for i in range(1, month_list[m-1] + 1 + flag):
        print(' %2d' % i, end="")
        blank += 1
        if blank % 7 == 0:
            print("")
    print("")