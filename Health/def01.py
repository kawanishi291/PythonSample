import datetime
dt_now = datetime.datetime.now()
year = dt_now.year
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    flag = 1
else:
    flag = 0

def calc(day, m):
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
    