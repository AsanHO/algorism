import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

while True:
    t = str(int(input()))
    if t == "0":
        break
    tr = "".join(reversed(list(t)))
    if(t == tr):
        print("yes")
    else:
        print("no")
        