import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(str, input().split())
    result = int(a[-1])**int(b[-1])
    if int(a) % 10 == 0:
        print(10)
    else:
        print(int(str(result)[-1]))
