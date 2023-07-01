import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

t = int(input())


def fib(n, cache={}):
    print(cache)
    if n == 1 or n == 2:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1, cache)+fib(n-2, cache)
    return cache[n]


print(fib(t))
