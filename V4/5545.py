import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

h2s = int(input())
s2p = int(input())
p2a = int(input())
a2h = int(input())

total_second = h2s+s2p+p2a+a2h

print(total_second//60)
print(total_second%60)