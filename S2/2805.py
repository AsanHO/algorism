import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
"""
1. 절단기에 높이 h지정
2. 톱날이 h위로 이동 그리고 절단 (낮은나무는 잘리지 않음)
3. 필요한만큼만 가져감.
4. 이분탐색을 변형해야할지도?
5. 답이 없는 경우 최댓값을 출력해야함
"""
result = []
left = 1
right = max(trees)
while left <= right:
    if left == 0 and right == 0:
        break
    mid = (left+right)//2
    cutted_trees = list(map(lambda x: x-mid if x >= mid else 0, trees))
    sum_cutted_trees = sum(cutted_trees)
    if sum_cutted_trees >= m:
        left = mid + 1
        result.append(mid)
    else:
        right = mid - 1
if len(result) == 0:
    print(0)
else:
    print(max(result))
