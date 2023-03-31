import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

n = int(input())
stack = []
answer = []
no = False
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        no = True
        break

if not no:
    for i in answer:
        print(i)
