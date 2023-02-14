import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline


t = int(input())
last = 0
current = 1
if t < 2:
    print(t)
else:
    for _ in range(t-1):
        temp = current
        current = last + current
        last = temp
    print(current)