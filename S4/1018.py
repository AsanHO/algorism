import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

n,m = map(int,input().split())
#n행 m열
t = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    t[i] = list(str(input().strip()))
print(t)
compare1 = [
    ["W","B","W","B","W","B","W","B",],
    ["B","W","B","W","B","W","B","W",],
    ["W","B","W","B","W","B","W","B",],
    ["B","W","B","B","B","W","B","W",],
    ["W","B","W","B","W","B","W","B",],
    ["B","W","B","W","B","W","B","W",],
    ["W","B","W","B","W","B","W","B",],
    ["B","W","B","W","B","W","B","W",],
]
compare2 = list(reversed(compare1))

for i in range(n-8):
    for i in range(m-8):
    
