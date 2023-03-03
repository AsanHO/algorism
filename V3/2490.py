import sys

os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

for _ in range(3):
    target = list(map(int, input().split()))
    count = 0
    for i in target:
        if i == 1:
            count += 1
    if count == 0:
        print("D")
    elif count == 1:
        print("C")
    elif count == 2:
        print("B")
    elif count == 3:
        print("A")
    elif count == 4:
        print("E")
