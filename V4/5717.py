import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

while True:
    m, f = map(int, input().split())
    if m == 0 and f == 0:
        break
    print(m+f)
