import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

k, n = map(int, input().split())
cables = []
for _ in range(k):
    cables.append(int(input()))

left = 1
right = max(cables)
count = 0
while left <= right:
    mid = (left+right)//2
    count = 0
    for cable in cables:
        count += cable // mid
    print(mid, count, n, left, right)
    if count < n:  # 케이블수가 필요한수보다 작다면 더 짧게 잘라야함
        right = mid - 1
    else:  # 케이블수가 필요한수보다 많다면 더 길게 잘라야함
        left = mid + 1

print(sum(list(map(lambda x: x//right, cables))))
print(right)
