import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

t = int(input())
for i in range(t):
    a, b = map(int, input().split(','))
    print(a+b)
