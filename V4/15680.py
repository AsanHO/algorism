import itertools
import datetime as dt
import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

print("YONSEI") if int(input()) == 0 else print(
    "Leading the Way to the Future")
