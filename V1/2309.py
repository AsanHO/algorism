import itertools
import datetime as dt
import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

combinations = itertools.combinations(dwarfs, 7)

for combination in combinations:
    if sum(combination) == 100:
        combination = list(combination)
        combination.sort()
        list(map(lambda x: print(x), combination))
        break
