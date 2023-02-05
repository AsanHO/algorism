import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

T = int(input())

print("*"*T)
j = 0
for i in range(T-1,0,-1):
    star = "*"*i
    blank = " "*j
    print(blank,star)
    j += 1