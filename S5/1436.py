import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

t = int(input())
init = 666

while t != 0:
    if "666" in str(init):
       t -= 1
    init = init + 1

print(init-1) 