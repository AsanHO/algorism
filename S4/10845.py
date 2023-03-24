import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

T = int(input())
deque = []
for _ in range(T):
    t = list(input().split())
    command = t[0]
    if command == "push":
        x = t[1]
        deque.append(x)
    elif command == "pop":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.remove(deque[0])
    elif command == "size":
        print(len(deque))
    elif command == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif command == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
