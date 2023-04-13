"""
그리디 알고리즘, 정렬
"""
import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
people.sort()
time = 0
result = 0
for i in people:
    time += i
    result += time
print(result)
