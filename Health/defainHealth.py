# カレンダーリスト
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def inputNumber(msg, MIN, MAX):
    while(1):
        num = int(input(msg))
        if(MIN <= num and num <= MAX):
            break
    return num


def LastDayOfTheMonth(y, m):
    if checkLeapYear(y) == 1 and m == 2:
        return 29
    else:
        return month_list[m-1]



# 周期計算
def calc(y, m, day):
    flag = checkLeapYear(y)
    month = 1
    while True:
        if day > month_list[m]:
            if flag == 1 and m == 1:
                day -= 29
            else:
                day -= month_list[m]
            m += 1
        else:
            break
    month += m

    return month, day

# 閏年カウント
def countLeapYear(year):
    cnt = 0
    for i in range(1900, year):
        cnt += checkLeapYear(i)

    return cnt

# 閏年判定
def checkLeapYear(num):
    if ((num % 4 == 0) and (num % 100 != 0)) or (num % 400 == 0):
        return 1
    else:
        return 0


# 総合日数カウント
def countAllDays(year, month, cnt):
    days = (year - 1900) * 365 + cnt
    for i in range(0, month-1):
        days += month_list[i]
    
    return days


# カレンダー表示
def printCalendar(y, m, blank):
    flag = checkLeapYear(y)
    print('\n        %d/%2d' %(y, m))
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