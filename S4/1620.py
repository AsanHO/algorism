import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

n, m = map(int, input().split())
# 포켓몬명
num_dic = {}
poke_dic = {}
for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])

# 알파벳이면 포켓몬 번호
# 번호가 들어오면 포켓몬 이름
