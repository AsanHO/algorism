import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

T = list(map(int,input().split(" ")))

T.sort()
for t in T:
    print(t,end=" ")