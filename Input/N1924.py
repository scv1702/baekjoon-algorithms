import sys

# 1월 1일 월요일
# 1, 3, 5, 7, 8, 10, 12월은 31일까지
# 4, 6, 8, 11월은 30일까지
# 2월은 28일까지

# 그렇다면, 매월 1일의 요일을 구하면 쉽게 가능할듯
day_of_week = [ 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT' ]

last_days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

# 매월 1일의 요일을 저장하는 리스트
first_dows = [ 1 ]

# 2월부터 매월 1일의 요일 계산
first_dow = first_dows[0]
for last_day in last_days:
    last_dow = first_dow + last_day % 7 - 1

    if last_dow + 1 >= len(day_of_week):
        first_dow = last_dow + 1 - 7
        last_dow -= 7
    else:
        first_dow = last_dow + 1

    first_dows.append(first_dow)

now_month, now_day = map(int, sys.stdin.readline().split())

# 현재 요일 계산
temp = first_dows[now_month - 1] + (now_day % 7 - 1)

if temp >= len(day_of_week):
    temp -= 7

print(day_of_week[temp])