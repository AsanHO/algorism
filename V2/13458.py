import math
import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
# 총감독관,부감독관 감시자 수
result = 0
# 총감독관 한명만 있을수도 있음
for i in a:
    if i < b:
        result += 1
    else:
        i -= b
        result += 1+math.ceil(i / c)
print(result)
