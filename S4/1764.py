import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

n, m = map(int, input().split())
hash = {}
result = []
for _ in range(n):
    name = input().rstrip()
    hash[name] = 1
for _ in range(m):
    name = input().rstrip()
    if name in hash.keys():
        result.append(name)
print(len(result))
result.sort()
for i in result:
    print(i)
