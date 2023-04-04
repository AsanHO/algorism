import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

"""
"""
n = int(input())
for i in range(n-1, 1, -1):
    n *= i
n = list(reversed(str(n)))
count = 0
if n == ['0']:
    print(count)
else:
    for i in n:
        if i == "0":
            count += 1
        else:
            break
    print(count)
