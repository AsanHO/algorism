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

while left <= right:
    mid = (left+right)//2
    count = 0
    for i in cables:
        count += i // mid  # 각 랜선을 미드로 나눠서 더함
    if count >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)
