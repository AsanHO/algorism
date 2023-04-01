import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

"""
나라시
n세로
m가로
왼쪽위 좌표 0,0
추가는 1초 제거는 2초
가장 빈도수가 많은 높이가 기준이 되어야함
"""
n, m, b = map(int, input().split())
# b = 인벤토리
ground = []
for _ in n:
    arr = list(map(int, input().split()))
    ground += arr

print(ground)
