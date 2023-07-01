import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

t = list(input())

# 홀수면 가운데 자름
if len(t) % 2 == 1:
    del t[len(t)//2]
# 가운데를 기준으로 자름
left = t[:len(t)//2]
right = t[len(t)//2:]

if left == list(reversed(right)):
    print(1)
else:
    print(0)
