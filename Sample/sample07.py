from def07 import *

year = int(input("西暦 => "))
month = int(input("月 => "))
cnt = countLeapYear(year)
days = countAllDays(year, month, cnt)
blank = (days + 1) % 7
printCalendar(year, month, blank)