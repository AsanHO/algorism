import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

T = int(input())
s = []
for _ in range(T):
    t = list(input().split())
    x = 0
    command = t[0]
    if len(t) > 1:
        x = int(t[1])
    if command == "add":
        if x not in s:
            s.append(x)
    elif command == "remove":
        if x in s:
            s.remove(x)
    elif command == "check":
        if x in s:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if x in s:
            s.remove(x)
        else:
            s.append(x)
    elif command == "all":
        s = []
        s = [i for i in range(1, 21)]
    elif command == "empty":
        s = []


# 1 1
# 1 1
# 0 0
# 1 1
# 0 0
# 1 1
# 0 0
# 1 1
# 0 0
# 1 1
# 1 1
# 0 0
# 0 0
# 0 0
# 1 1
# 0 0
