import datetime as dt
import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

t = int(input())
result = 0
for _ in range(t):
    answer = int(input())
    result += 1 if answer == 1 else -1

print("Junhee is cute!")if result > 0 else print("Junhee is not cute!")
