import datetime as dt
import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

m, d = map(int, input().split())

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN",]

print(days[dt.date(2007, m, d).weekday()])
