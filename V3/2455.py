import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

train = 0
max = 0
for i in range(4):
    OUT, IN = map(int, input().split())
    train -= OUT
    train += IN
    if train >= max:
        max = train
print(max)
