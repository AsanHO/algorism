import sys

os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

target = list(str(input()))

init = 0
for i in target:
    print(i,end="")
    init += 1
    if init == 10:
        init=0
        print(end="\n")
        