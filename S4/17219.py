"""
hash
"""
import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

n, m = map(int, input().split())
hash = {}
for _ in range(n):
    url, pw = map(str, input().split())
    hash[url] = pw
for _ in range(m):
    url = input().rstrip()
    print(hash[url])
