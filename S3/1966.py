from collections import deque
import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # enumerate함수, 리스트에 번호를 부여
    docs = deque(enumerate(map(int, input().split())))

    count = 0
    while True:
        print(docs, count)
        doc = docs.popleft()
        if any(doc[1] < i[1]for i in docs):
            docs.append(doc)
        else:
            count += 1
            if doc[0] == m:
                print(count)
                break
