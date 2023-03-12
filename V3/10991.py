import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

t = int(input())
blank = t-1
for i in range(1, t+1):
    cell = "* "
    print(" "*blank + cell*i, end="\n")
    blank -= 1
# print문에서 ,을 사용하면 자동으로 띄어쓰기가 됨
