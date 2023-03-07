import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

t = 1000-int(input())
count = t//500
t = t % 500
count = count + t//100
t = t % 100
count = count + t//50
t = t % 50
count = count + t//10
t = t % 10
count = count + t//5
t = t % 5
count = count + t//1
t = t % 1
print(count)
