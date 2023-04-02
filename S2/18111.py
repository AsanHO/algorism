import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

"""

"""
n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize  # 일반 정수형보다 커야함
idx = 0
# b = 인벤토리
print(graph)
for floor in range(257):  # 1
    # 깎는양, 쌓는양
    del_floor, add_floor = 0, 0
    for i in range(n):
        for j in range(m):
            target = graph[i][j]
            # 2 좌표가 기준높이보다 크면 깎는양은 깎임
            if target >= floor:
                del_floor += target - floor
            # 기준높이보다 작다면 쌓는양도 깎임
            else:
                add_floor += floor - target
    # 깎는양 + 인벤토리 = 최종인벤토리가 쌓는양보다 커야만 나라시가능
    if del_floor + b >= add_floor:
        # 최종적으로 걸리는 시간
        time = add_floor + del_floor * 2
        print(del_floor, add_floor, time, floor)
        if time <= answer:
            answer = time
            idx = floor
print(answer, idx)
