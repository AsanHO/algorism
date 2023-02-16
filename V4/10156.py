import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

k,n,m = map(int,input().split())
result = n*k-m
if result > 0:
    print(result)
else:
    print(0)